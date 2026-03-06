import nmap


def scan_network(network: str, ports: str = "22,80,443,445,3389") -> None:
    scanner = nmap.PortScanner()

    print(f"\nScanning {network} on ports {ports}...\n")

    scanner.scan(hosts=network, arguments=f"-n -Pn --open -p {ports}")

    found_any = False

    for host in scanner.all_hosts():
        if scanner[host].state() != "up":
            continue

        open_ports = []

        for proto in scanner[host].all_protocols():
            for port in sorted(scanner[host][proto].keys()):
                port_state = scanner[host][proto][port]["state"]
                if port_state == "open":
                    open_ports.append(f"{proto.upper()}:{port}")

        if open_ports:
            found_any = True
            print(f"{host} -> {', '.join(open_ports)}")

    if not found_any:
        print("No open ports found on the selected ports list.")


def main() -> None:
    print("Advanced Network Scanner")
    network = input("Enter network range (example 10.0.0.0/24): ").strip()

    if not network:
        print("Error: network range cannot be empty.")
        return

    scan_network(network)


if __name__ == "__main__":
    main()
