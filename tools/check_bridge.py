#!/usr/bin/env python3
"""Read-only smoke test against an explicitly specified private lab C5."""
import argparse
import ipaddress
import secrets
import socket
import time

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host")
    args = parser.parse_args()
    ip = ipaddress.IPv4Address(args.host)
    allowed = ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")
    if not any(ip in ipaddress.IPv4Network(net) for net in allowed):
        parser.error("Specify your own C5's RFC1918 IPv4 address")
    ident = secrets.token_hex(4)
    begin, end = f"@C5 BEGIN {ident}".encode(), f"@C5 END {ident}".encode()
    with socket.create_connection((str(ip), 2323), timeout=5) as sock:
        sock.sendall(f"@C5 {ident} PING\n".encode())
        deadline = time.monotonic() + 15
        data = bytearray()
        while time.monotonic() < deadline and len(data) < 65536:
            sock.settimeout(max(0.01, deadline - time.monotonic()))
            block = sock.recv(min(4096, 65536 - len(data)))
            if not block:
                break
            data.extend(block)
            lines = data.splitlines()
            if begin in lines and end in lines:
                start = lines.index(begin)
                finish = lines.index(end)
                if start < finish and b"PONG FROM ESP32-C5" in lines[start+1:finish]:
                    print("PASS: matching C5 PING response")
                    return
                break
        raise SystemExit("FAIL: incomplete or unexpected PING response")

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        raise SystemExit(f"FAIL: {exc}")
