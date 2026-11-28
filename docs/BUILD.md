# Build and installation

Baseline: upstream BitPirate v1.8 commit `8a91778e25b699c59f34542d8ea8d405fa7e4020` and C5 v6.5-dual-node-candidate. The S3 integration is v6.6. The v6.7 bridge-safe candidate is a C5-only upgrade; the exact source package is not yet committed.

## C5

Reference hardware: ESP32-C5 DevKitC-1 N8R8 (DOIT/HW-983 variant), advertised 8 MB flash and 8 MB PSRAM, dual USB-C with integrated antenna. See the [reference hardware section](../README.md#hardware-and-setup). The advertised PSRAM capacity is not a verified firmware memory setting; retain the working configuration.

For a working v6.6 system, keep the Cardputer image unchanged. Preserve the configured v6.5 rollback sketch and Arduino settings. Use ESP32C5 Dev Module and keep Zigbee Mode Disabled. Do not alter flash size, PSRAM or partition scheme for v6.7. After uploading the C5, confirm VERSION, bridge status, SELFTEST and PING; perform the remaining regression checks before accepting the build.

Use Arduino IDE with a compatible ESP32-C5 board core and ArduinoJson. Preserve the board/partition configuration of a known working build. The tested C5 board used the UART USB-C port for upload. Set your own Wi-Fi credentials locally in the sketch; never commit them. Verify the firmware before uploading and check VERSION and PING on TCP 2323 on your isolated LAN.

## Cardputer ADV

Use Python 3.13 and PlatformIO (the development build used PlatformIO 6.2.0). Clone the exact upstream tag:

```sh
git clone --branch v1.8 --depth 1 https://github.com/geo-tp/ESP32-Bit-Pirate.git BitPirate-v1.8
```

The v6.5 adapter installer and v6.6 mode installer must run from the complete source package, in that order, against this checkout. Run each with --check before applying it. The mode installer preserves the pre-mode-26 sources and available binaries in a sibling backup directory. Do not rerun the original baseline check after a successful install.

The Cardputer ADV display correction used rotation 0 in both src/Boards/Cardputer/CardputerBoard.cpp and src/Views/Cardputer/CardputerTerminalView.cpp (verify the actual second path in your checkout before editing). Preserve the validated display configuration.

```sh
cd BitPirate-v1.8
python -m platformio run -e cardputer-adv
```

Only after a successful build, place the Cardputer in download mode with G0 and confirm its serial port. Use the actual port, not a hard-coded port from another machine:

```sh
python -m platformio device list
python -m platformio run -e cardputer-adv -t upload --upload-port YOUR_PORT
```

Keep the original firmware and source backups. Never flash the C5 image to the Cardputer or vice versa.

Reference: [upstream build guide](https://github.com/geo-tp/ESP32-Bit-Pirate/wiki/99-Build).
