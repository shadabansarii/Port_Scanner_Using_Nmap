import nmap
import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port_range(port_range):
    try:
        start, end = map(int, port_range.split('-'))
        if 0 < start <= end <= 65535:
            return start, end
    except:
        pass
    return None

def scan_network(target_ip, start_port, end_port):
    nm = nmap.PortScanner()
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")
    try:
        nm.scan(target_ip, f"{start_port}-{end_port}")
    except Exception as e:
        print(f"Scanning failed: {e}")
        return

    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                if nm[host][proto][port]['state'] == 'open':
                    print(f"Open Port: {port}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ").strip()
    if not validate_ip(target_ip):
        print("Invalid IP address. Exiting.")
        exit()

    port_range = input("Enter port range (e.g., 20-1000): ").strip()
    port_limits = validate_port_range(port_range)
    if not port_limits:
        print("Invalid port range. Exiting.")
        exit()

    start_port, end_port = port_limits
    scan_network(target_ip, start_port, end_port)
