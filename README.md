# Fuzzing Program for IoT Device

Author: Alon Gritsovsky

## Description

This fuzzing program is designed to mutate different packets and send them to an IoT device. It utilizes the pyradamsa library for packet mutation and allows for continuous packet sending to test the device's resilience against various inputs.

## Prerequisites

- Python 3.x
- pyradamsa library

## Usage

1. Enter the IP address of the server where the IoT device is connected.
2. Enter the source port number for the server.
3. Ensure that the desired packets for fuzzing are available in the "fuzzer_packet" folder.
4. Run the script and wait for a client to connect to the server.
5. The script will continuously mutate and send packets to the connected client.
6. Monitor the mutated packets and their effects on the IoT device.

## Folder Structure

- **fuzzer_packet**: Contains the packet files for fuzzing.

## Notes

- This program is designed for testing purposes only and should be used responsibly.
- Use caution when performing fuzzing activities on production systems.
- Ensure that you have appropriate permissions and legal rights to perform testing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

##Author
Alon Gritsovsky
