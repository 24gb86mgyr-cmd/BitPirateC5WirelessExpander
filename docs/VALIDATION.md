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

## v6.7 candidate — subsequent test on 2026-11-28

Observed: the existing mode 26 remained available. Missing C5 host and disconnected local Wi-Fi were reported correctly. After configuring the host and connecting through mode 14, WEXP returned the expanded ls command inventory and a complete response frame. This demonstrates the new command path but does not establish the execution of every listed command.

Host-side package tests: 56 frame/alias/lookup assertions, 4 synthetic installer transforms, 15 mocked adapter assertions. No claim of full firmware cross-compilation by the host tests.

### Remaining v6.7 acceptance checks

Run individually through WEXP on an authorized lab network:

```text
version
bridge status
selftest
ping
wifi help
wifi info
wifi channel
wifi scan 5
wifi scan 24
wifi dns example.com
lookup ip 192.168.1.1
lookup mac 02:00:00:00:00:01
4cast 02129
ping
```

Expect version v6.7-bridge-safe-candidate, lock ON, SELFTEST 15/15 PASS and successful final PING. Check local LoRa and existing modes separately. No raw discovery logs or credentials should be published. Do not classify the candidate as fully hardware-validated until regression results are recorded.
