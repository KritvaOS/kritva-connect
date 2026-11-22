"""Checks for the DRAFT v0.1.0 Connect contracts (cross-repository review required).

Software checks of the draft schemas only. Not hardware or safety validation.
Needs the jsonschema package (with its referencing dependency).
"""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_FILES = [
    "media-session/participant-identity.schema.json",
    "media-session/join-grant.schema.json",
    "media-session/track-descriptor.schema.json",
    "media-session/session-event.schema.json",
    "telemetry-delivery/envelope.schema.json",
]


def load():
    schemas = {}
    registry = Registry()
    for rel in SCHEMA_FILES:
        doc = json.loads((ROOT / rel).read_text())
        schemas[rel] = doc
        registry = registry.with_resource(doc["$id"], Resource.from_contents(doc))
    return schemas, registry


SCHEMAS, REGISTRY = load()


def validator(rel):
    return Draft202012Validator(SCHEMAS[rel], registry=REGISTRY)


def valid(rel, doc):
    return validator(rel).is_valid(doc)


IDENT = "robot:dev-001:sess-42"
NOW = "2026-11-22T14:30:00Z"


def check_delivery_order(envelopes):
    """Receiver-side rule from contract/README.md: per (channel_id, channel_epoch),
    a delivery_sequence greater than previous + 1 is a missing range. Never compares
    across epochs. Returns a list of (channel_id, epoch, first_missing, last_missing)."""
    last = {}
    missing = []
    for e in envelopes:
        d = e["delivery"]
        if e["kind"] == "gap_notice":
            assert e["missing_to"] >= e["missing_from"], "gap_notice range is inverted"
            continue
        key = (d["channel_id"], d["channel_epoch"])
        seq = d["delivery_sequence"]
        if key in last:
            prev = last[key]
            if seq <= prev:
                raise ValueError("delivery_sequence did not increase within an epoch")
            if seq > prev + 1:
                missing.append((key[0], key[1], prev + 1, seq - 1))
        last[key] = seq
    return missing


class SchemaValidity(unittest.TestCase):
    def test_every_schema_is_valid_2020_12(self):
        for rel, doc in SCHEMAS.items():
            Draft202012Validator.check_schema(doc)

    def test_every_schema_is_marked_draft(self):
        for rel, doc in SCHEMAS.items():
            self.assertIn("DRAFT", doc["title"], rel)
            self.assertIn("CROSS-REPOSITORY REVIEW REQUIRED", doc["title"], rel)


class Identity(unittest.TestCase):
    f = "media-session/participant-identity.schema.json"

    def test_accepts(self):
        self.assertTrue(valid(self.f, IDENT))

    def test_rejects(self):
        for bad in ["robot:dev:", "robot::s", "operator:dev:s", "robot:de v:s", "robot:dev:s:x", "", "robot:" + "a" * 65 + ":s"]:
            self.assertFalse(valid(self.f, bad), bad)


class JoinGrant(unittest.TestCase):
    f = "media-session/join-grant.schema.json"
    good = {
        "contract_version": "0.1.0",
        "server_url": "wss://example.invalid",
        "session_ref": "sess-42",
        "participant_identity": IDENT,
        "token": "x",
        "token_expires_at": NOW,
        "media_capabilities": ["video", "telemetry"],
    }

    def test_accepts(self):
        self.assertTrue(valid(self.f, self.good))

    def test_no_admin_or_command_authority_field(self):
        for extra in ["room_admin", "can_command", "api_secret", "admin"]:
            self.assertFalse(valid(self.f, {**self.good, extra: True}), extra)

    def test_audio_is_not_a_v01_capability(self):
        self.assertFalse(valid(self.f, {**self.good, "media_capabilities": ["audio"]}))

    def test_requires_secure_url_and_valid_identity(self):
        self.assertFalse(valid(self.f, {**self.good, "server_url": "http://example.invalid"}))
        self.assertFalse(valid(self.f, {**self.good, "participant_identity": "someone"}))

    def test_missing_token_rejected(self):
        bad = dict(self.good)
        del bad["token"]
        self.assertFalse(valid(self.f, bad))


class TrackDescriptor(unittest.TestCase):
    f = "media-session/track-descriptor.schema.json"

    def test_video_and_data(self):
        self.assertTrue(valid(self.f, {"contract_version": "0.1.0", "track_id": "t1", "kind": "video", "state": "published"}))
        self.assertTrue(valid(self.f, {"contract_version": "0.1.0", "track_id": "t2", "kind": "data", "channel_id": "telemetry-01", "state": "pending"}))

    def test_data_needs_channel_and_video_must_not_have_one(self):
        self.assertFalse(valid(self.f, {"contract_version": "0.1.0", "track_id": "t2", "kind": "data", "state": "pending"}))
        self.assertFalse(valid(self.f, {"contract_version": "0.1.0", "track_id": "t1", "kind": "video", "channel_id": "telemetry-01", "state": "pending"}))


class SessionEvent(unittest.TestCase):
    f = "media-session/session-event.schema.json"
    base = {
        "contract_version": "0.1.0",
        "state_scope": "transport",
        "event": "joined",
        "occurred_at": NOW,
        "session_ref": "sess-42",
        "participant_identity": IDENT,
    }

    def test_accepts(self):
        self.assertTrue(valid(self.f, self.base))

    def test_scope_must_be_transport(self):
        for scope in ["safety", "business", "session"]:
            self.assertFalse(valid(self.f, {**self.base, "state_scope": scope}), scope)

    def test_token_refresh_failed_needs_error_with_known_category(self):
        ev = {**self.base, "event": "token_refresh_failed"}
        self.assertFalse(valid(self.f, ev))
        self.assertTrue(valid(self.f, {**ev, "error": {"category": "auth", "code": "token_refresh_failed"}}))
        self.assertFalse(valid(self.f, {**ev, "error": {"category": "safety", "code": "x"}}))

    def test_no_safety_or_command_events(self):
        for name in ["robot_safe", "estop", "command_ack", "lease_granted"]:
            self.assertFalse(valid(self.f, {**self.base, "event": name}), name)


class TelemetryEnvelope(unittest.TestCase):
    f = "telemetry-delivery/envelope.schema.json"

    @staticmethod
    def data(seq, epoch=0, channel="telemetry-01"):
        return {
            "contract_version": "0.1.0",
            "kind": "data",
            "delivery": {"channel_id": channel, "channel_epoch": epoch, "delivery_sequence": seq, "gateway_sent_at": NOW},
            "sense_stream_version": "0.1.0",
            "sense_record": {"record": "sample", "index": 1},
        }

    @staticmethod
    def gap(a, b):
        return {
            "contract_version": "0.1.0",
            "kind": "gap_notice",
            "delivery": {"channel_id": "telemetry-01", "channel_epoch": 0, "gateway_sent_at": NOW},
            "missing_from": a,
            "missing_to": b,
            "reason": "dropped_lossy_channel",
        }

    def test_accepts_data_and_gap(self):
        self.assertTrue(valid(self.f, self.data(0)))
        self.assertTrue(valid(self.f, self.gap(3, 5)))

    def test_sense_record_is_opaque_but_must_be_an_object(self):
        bad = self.data(0)
        bad["sense_record"] = "text"
        self.assertFalse(valid(self.f, bad))

    def test_envelope_cannot_carry_sense_semantics(self):
        bad = self.data(0)
        bad["sample_sequence"] = 7
        self.assertFalse(valid(self.f, bad))
        bad = self.data(0)
        bad["delivery"]["sense_sequence"] = 7
        self.assertFalse(valid(self.f, bad))

    def test_negative_sequence_rejected(self):
        self.assertFalse(valid(self.f, self.data(-1)))

    def test_missing_range_detected_within_an_epoch(self):
        seq = [self.data(0), self.data(1), self.data(4), self.data(5)]
        self.assertEqual(check_delivery_order(seq), [("telemetry-01", 0, 2, 3)])

    def test_epoch_reset_is_not_a_gap(self):
        seq = [self.data(0), self.data(1), self.data(0, epoch=1), self.data(1, epoch=1)]
        self.assertEqual(check_delivery_order(seq), [])

    def test_regression_within_an_epoch_is_an_error(self):
        with self.assertRaises(ValueError):
            check_delivery_order([self.data(0), self.data(1), self.data(1)])

    def test_inverted_gap_range_is_caught_by_the_rule_check(self):
        with self.assertRaises(AssertionError):
            check_delivery_order([self.gap(5, 3)])


if __name__ == "__main__":
    unittest.main()
