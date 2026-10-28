import socket
import ipaddress

def is_valid_ip(ip_str):
    # Track 1 fix 1 & 2: strip /24 and len check (like your login-system.py fix)
    clean_ip = ip_str.split('/')[0]
    parts = clean_ip.split('.')
    if len(parts) != 4:
        return False, f"Invalid: len={len(parts)}, needs 4"
    try:
        ip = ipaddress.ip_address(clean_ip)
        return True, f"{ip} is valid IPv{ip.version}"
    except ValueError:
        return False, f"{clean_ip} is invalid"

def check_host(ip, port=53, timeout=3):
    # Track 1 fix 3: DNS with gethostbyname + try/except
    try:
        resolved = socket.gethostbyname(ip)
        print(f"DNS: {ip} -> {resolved}")
    except socket.gaierror as e:
        print(f"❌ DNS fail for {ip}: {e}")
        return

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            print(f"✅ {ip}:{port} reachable - Network OK!")
        else:
            print(f"⚠️ {ip}:{port} not reachable - check internet/firewall")
    except Exception as e:
        print(f"Error: {e}")

# --- Tests ---
print("=== Neo's Network Checker v2 ===")
tests = ["8.8.8.8", "192.168.1.10", "192.168.0.1/24", "999.999.999.999", "google.com"]

for t in tests:
    if "." in t and t[0].isdigit():
        valid, msg = is_valid_ip(t)
        print(f"{msg}")
        if valid:
            check_host(t.split('/')[0])
    else:
        print(f"\nTesting domain: {t}")
        check_host(t)
    print("-")

print("\nDone - This is what IT Support does daily! - Neo Rampai")
