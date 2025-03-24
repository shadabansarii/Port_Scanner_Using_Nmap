import nmap  

def scan_network(target):  
    nm = nmap.PortScanner()  
    nm.scan(target, '1-1024')  # Scan ports 1-1024  

    for host in nm.all_hosts():  
        print(f"\nHost: {host} ({nm[host].hostname()})")  
        print(f"State: {nm[host].state()}")  

        for proto in nm[host].all_protocols():  
            print(f"\nProtocol: {proto}")  
            ports = nm[host][proto].keys()  
            for port in ports:  
                print(f"Port: {port}, State: {nm[host][proto][port]['state']}")  

# Run the script  
target_ip = input("Enter target IP: ")  
scan_network(target_ip)
