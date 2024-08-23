from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import threading


# Callback function to process each captured packet
def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        # Determine the protocol
        if protocol == 6:  # TCP
            protocol_name = 'TCP'
        elif protocol == 17:  # UDP
            protocol_name = 'UDP'
        else:
            protocol_name = 'Other'

        # Print packet details
        print(f"Source: {src_ip} -> Destination: {dst_ip} | Protocol: {protocol_name}")

        # Print payload data if present
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload) if packet.haslayer(TCP) else bytes(packet[UDP].payload)
            print(f"Payload: {payload}\n")


# Function to stop sniffing after a certain duration
def stop_sniffing(sniffer):
    sniffer.stop()


# Start sniffing packets
print("Starting packet sniffer...")

# Create a sniffer object
sniffer = sniff(prn=packet_callback, filter="ip", store=False, count=0, timeout=10)

# Set a timer to stop the sniffer after 10 seconds
timer = threading.Timer(10, stop_sniffing, [sniffer])
timer.start()

# Run the sniffer
sniffer
print("Sniffer stopped.")
