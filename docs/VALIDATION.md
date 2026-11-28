# Hardware validation — 2026-11-28

Configuration: M5Stack Cardputer ADV running patched BitPirate v1.8 (v6.6 S3 integration), ESP32-C5 running v6.5-dual-node-candidate.

Observed in terminal output:

- Mode 26 appeared in the ordinary mode selector; WEXP prompt and integrated help appeared.
- Local Wi-Fi connected; configured C5 host; PING returned PONG.
- Three ZIP-code weather queries returned forecast fields and completed response frames.
- SELFTEST reported 15/15 PASS; VERSION and version both returned the expected C5 version.
- Band-specific scans completed: 21 matching 2.4 GHz APs and 13 matching 5 GHz APs in the test environment. Results vary by location.
- Unsupported commands returned a framed error.
- Returned to WIFI and reentered WEXP; exit returned to HIZ.

No private SSIDs, BSSIDs, credentials or raw scan output are included.

Not yet verified: full upstream regression coverage, attached LoRa cap operation after all mode transitions, web terminal operation, long-duration reliability, concurrency, reconnect behavior after outages, authentication, repeat/macro integration, every supported diagnostic command. Internal self-test coverage is not equivalent to a full integration test.
