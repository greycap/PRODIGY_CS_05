# PackCap

**PackCap** is a simple packet sniffer tool that captures and analyzes network packets. It displays relevant information such as source and destination IP addresses, protocols, and payload data. **This tool is intended for educational purposes only. Use responsibly and ensure you have the necessary permissions to sniff network traffic.**

## Features

- Captures network packets on the local interface.
- Displays source and destination IP addresses.
- Identifies the protocol (TCP, UDP, etc.).
- Prints payload data if available.
- Automatically stops after a specified duration.

## Installation

To use this tool, you need to have Python and `scapy` installed. Follow these steps:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).
2. **Install Scapy**: Open your terminal or command prompt and run:
   ```bash
   pip install scapy
   ```

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/greycap/PRODIGY_CS_05
   ```

2. **Run the Sniffer**: Execute the script with Python. You may need to run it with elevated privileges (e.g., `sudo` on Linux/Mac or as an Administrator on Windows).
   ```bash
   python3 packcap.py
   ```

3. **Output**: The sniffer will run for 10 seconds, capturing and displaying packet details in the console.

## Ethical Considerations

Please ensure you have the necessary permissions to sniff network traffic. Unauthorized network sniffing is illegal and unethical. This tool is provided for educational purposes to help users learn about network traffic analysis.
