import pydivert

# Define a filter to drop HTTP traffic
filter = "tcp.DstPort == 443"

with pydivert.WinDivert(filter) as w:
    for packet in w:
        print(packet)  # Print the packet for debugging purposes
        if packet.dst_port == 443:
            continue  # Drop the packet
        w.send(packet)
