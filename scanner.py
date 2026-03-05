import nmap

print("Advanced Network Scanner")

network = input("Enter network range (example 192.168.1.0/24): ")

scanner = nmap.PortScanner()

print("Scanning network...")

scanner.scan(hosts=network, arguments='-p 22,80,443')

for host in scanner.all_hosts():
    print("\nHost:", host)
    print("State:", scanner[host].state())

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()

        for port in ports:
            state = scanner[host][proto][port]['state']
            print(f"Port {port} is {state}")
