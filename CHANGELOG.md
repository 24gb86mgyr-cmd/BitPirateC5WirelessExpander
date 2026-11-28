# Changelog

Internal development revisions, not published semantic-versioned releases.

## v6.7 — 2026-11-28

- C5-only compatibility expansion; v6.6 Cardputer image unchanged.
- Added framed command aliases including ls, wifi help, wifi scan 5, wifi scan 24, CSV and channel scan forms, and Wi-Fi-prefixed diagnostics.
- Added local IPv4/MAC classification without external lookup requests.
- Bridge lock, TCP framing, listener, client lifecycle, Wi-Fi setup and radio drivers unchanged from v6.5; Zigbee remains disabled.
- Host validation: 56 frame/alias/lookup assertions, 4 synthetic installer transformations and 15 mocked S3 adapter assertions (75 total).
- Hardware evidence: mode 26 retained, missing host and Wi-Fi checks, successful ls inventory and complete response frame.
- Full hardware regression, VERSION, lock status and self-test on the new C5 build still pending. The intermittent session stall remains unresolved.

## v6.6 — 2026-11-28

- Native WIRELESS EXPANDER mode appended as mode 26; original 25 modes retained.
- WEXP prompt, integrated help and prefix-free remote diagnostic commands.
- Existing global c5 command and v6.5 C5 transport retained.
- Hardware validation: PING, VERSION, weather lookups, both Wi-Fi bands, self-test 15/15, unsupported command handling and mode switching.
- Remaining limitations: volatile host address, exact syntax, synchronous requests, no authentication, unresolved intermittent connection hang, no exhaustive regression test.

## v6.5

- One-shot TCP command framing with request identifiers.
- Global c5 diagnostic route in BitPirate v1.8.
- Verified physical Cardputer-to-C5 communication.
