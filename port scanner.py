import socket
from datetime import datetime
import threading

def port_scanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Set a timeout for the connection attempt
        if s.connect_ex((host, port)) == 0:
            print(f"Port {port} is open on {host}.")
            open_ports.append(port)
        else:
            closed_ports.append(port)
    except Exception as e:
        print(f"Error scanning port {port} on {host}: {e}")
    finally:
        s.close()

def scan_ports(host, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=port_scanner, args=(host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    host = input("Please enter the IP you want to scan: ")
    try:
        socket.inet_aton(host)  # Validate IP address
    except socket.error:
        print("Invalid IP address.")
        exit()

    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range.")
    except ValueError as e:
        print(f"Error: {e}")
        exit()

    open_ports = []
    closed_ports = []

    print(f"Starting scan on {host} from port {start_port} to {end_port}...")
    start_time = datetime.now()

    scan_ports(host, start_port, end_port)

    end_time = datetime.now()
    print("\nScan completed.")
    print(f"Open ports: {open_ports}")
    print(f"Closed ports: {len(closed_ports)}")
    print(f"Time taken: {end_time - start_time}")
