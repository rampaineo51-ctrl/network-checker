import socket
import ipaddress

# Your test IPs
test_ip = "8.8.8.8"  # Google DNS - should be reachable
my_ip = "192.168.1.10"  # Example local IP

# 1. Check if IP is valid
try:
    ip = ipaddress.ip_address(test_ip)
    print(f"✅ {ip} is a valid {ip.version} address")
except ValueError:
    print(f"❌ {test_ip} is invalid")

# 2. Try to connect (port 53 DNS)
def check_host(ip, port=53, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            print(f"✅ {ip}:{port} is reachable — Network OK!")
        else:
            print(f"⚠️ {ip}:{port} not reachable — check internet/firewall")
    except Exception as e:
        print(f"Error: {e}")

check_host(test_ip)
check_host(my_ip)

print("\nDone — This is what IT Support does daily!")
