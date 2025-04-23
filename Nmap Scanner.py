import nmap

scanner = nmap.PortScanner()
print("Welcome, this is a simple Nmap automation tool")
print("<-------------------------------------------------->")

ipaddr = input("Please enter an IP address you want to scan: ")
print(f"The IP entered is {ipaddr}")

while True:
    print("""
    Please enter the type of scan you want to run:
    1) SYN ACK Scan (-sS)
    2) Quick Scan (Top 100 ports)
    3) Full Intense Scan (All ports, OS & version detection, scripts, traceroute)
    Type 'exit' to quit
    """)

    resp = input("Your choice: ").strip()
    print(f"The selected option is: {resp}")

    if resp == '1':
        print("Running SYN ACK Scan...")
        scanner.scan(ipaddr, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("IP Status:", scanner[ipaddr].state())
        print("Protocols:", scanner[ipaddr].all_protocols())
        print("Open TCP Ports:", scanner[ipaddr]['tcp'].keys())

    elif resp == '2':
        print("\nRunning Quick Scan...")
        scanner.scan(ipaddr, arguments='-T4 -F')
        print(scanner.scaninfo())
        print("IP Status:", scanner[ipaddr].state())
        protocols = scanner[ipaddr].all_protocols()
        if protocols:
            for proto in protocols:
                ports = scanner[ipaddr][proto].keys()
                print(f"Open {proto.upper()} Ports:", list(ports))
        else:
            print("No open ports found.")

    elif resp == '3':
        print("Running Full Intense Scan.")
        scanner.scan(ipaddr, '1-65535', '-T4 -A -v')
        print(scanner.scaninfo())
        print("IP Status:", scanner[ipaddr].state())
        print("Protocols:", scanner[ipaddr].all_protocols())
        for proto in scanner[ipaddr].all_protocols():
            print(f"Open {proto.upper()} Ports:", scanner[ipaddr][proto].keys())

    elif resp.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3 or type 'exit' to quit.")
