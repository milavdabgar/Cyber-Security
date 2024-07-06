import pydivert
import socket

# Function to resolve domain name to IP address
def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        print(f"Error: Unable to resolve IP address for domain '{domain}'")
        return None

# Define the domain to block
blocked_domain = "facebook.com"

# Resolve the domain to get its IP address
blocked_ip = resolve_domain(blocked_domain)

if blocked_ip:
    # Create a filter to block outgoing traffic to the IP address of the domain
    filter = f"ip.DstAddr == '{blocked_ip}'"

    try:
        # Open a handle to the network stack with the specified filter
        with pydivert.WinDivert(filter) as w:
            print(f"Blocking traffic to {blocked_domain} (IP: {blocked_ip})...")
            for packet in w:
                # Drop the packet
                print(f"Blocking packet to {packet.dst_addr}")
                continue  # Do not forward the packet
    except Exception as e:
        print("An error occurred:", e)
else:
    print("Cannot block traffic. Domain resolution failed.")
