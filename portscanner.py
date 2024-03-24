import socket

class PortScanner:
    def __init__(self):
        pass

    def is_port_open(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def scan_ports(self, ip, port_range):
        try:
            print("Scanning ports...")
            for port in port_range:
                if self.is_port_open(ip, port):
                    print(f"{ip} {port} working")
                else:
                    print(f"{ip} {port} not working")
        except Exception as e:
            print(f"An error occurred: {e}")

    def scan_nearby_ips(self, ip, port_range):
        open_ports = {}
        try:
            for i in range(1, 255):
                target_ip = f"{ip[:-1]}{i}"
                open_ports[target_ip] = self.scan_ports(target_ip, port_range)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    scanner = PortScanner()
    while True:
        print("1. IP port scanning")
        print("2. Scan nearby IPs and ports")
        choice = input("Enter your choice: ")

        if choice == '1':
            target_ip = input("Enter the target IP address: ")
            port_range = [int(port) for port in input("Enter the port range (e.g., 80,443): ").split(",")]
            scanner.scan_ports(target_ip, port_range)
        elif choice == '2':
            target_ip = input("Enter the target IP address (e.g., 192.168.1.): ")
            port_range = [int(port) for port in input("Enter the port range (e.g., 80,443): ").split(",")]
            scanner.scan_nearby_ips(target_ip, port_range)
        else:
            print("Invalid choice. Please try again.")