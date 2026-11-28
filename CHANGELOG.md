# Changelog

Internal development revisions, not published semantic-versioned releases.

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
