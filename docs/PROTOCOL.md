# C5 one-shot protocol

Transport: TCP port 2323 on the private IPv4 address of the ESP32-C5.

```text
@C5 1234abcd PING
@C5 BEGIN 1234abcd
PONG FROM ESP32-C5
@C5 END 1234abcd
```

Request identifiers are eight hexadecimal characters. A request line contains the prefix, identifier, space, command and newline. The S3 adapter accepts 1–115 printable ASCII command characters. It ignores lines before the matching BEGIN marker, prints response lines and ends on the matching END marker.

The adapter uses a 2-second connection timeout, 45-second response deadline and 64 KiB receive cap. Individual displayed lines are capped at 512 characters. A completed frame can contain an error; it does not imply successful operation. Commands are one-shot, with no persistent remote submenu state.

The legacy interactive C5 shell shares port 2323; close other sessions before testing. A prior intermittent stall recovered after resetting test conditions; the root cause is not established.

No authentication or encryption is implemented. Use only a trusted isolated LAN.

## v6.7 compatibility

The wire format is unchanged. New aliases are normalized inside the framed diagnostic command layer, preserving argument case. The existing S3 adapter is reused. Bridge lock protects transport configuration; it is not authentication. The session lifecycle and its unresolved intermittent stall are unchanged.
