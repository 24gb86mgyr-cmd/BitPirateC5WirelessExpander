# Mode 25 to mode 26 compatibility

The wired [ESP32 Bus Expander](https://github.com/geo-tp/ESP32-Bus-Expander) uses UART independent of its Wi-Fi radio. WEXP uses that radio as its transport, so direct parity is not always appropriate.

| Capability | v6.7 status |
| --- | --- |
| 2.4 / 5 GHz discovery | Validated on v6.5; v6.7 regression pending |
| Wi-Fi status and channel diagnostics | Implemented |
| Flexible scan syntax and CSV aliases | Implemented; new aliases pending hardware tests |
| DNS, TCP, HTTP diagnostics | Implemented; hardware tests pending |
| IP/MAC lookup | Local classification only; no vendor/geolocation service |
| BLE discovery and status | Implemented; hardware tests pending |
| Wi-Fi connect/disconnect/reset/AP/repeater on remote C5 | Not exposed through framed diagnostic route; preserve control plane |
| Active RF disruption | Not a project goal |
| Zigbee/802.15.4 discovery | Separate experiment planned; disabled |
| Zigbee pairing, inspection and endpoint emulation | Deferred |

Bridge lock is a design constraint, not a substitute for authentication. Preserve the validated firmware and run regression tests before accepting future radio or transport changes. This is an independent project; no claim of official upstream compatibility or endorsement.
