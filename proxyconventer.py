import socks
import socket
import requests

class ProxyConverter:
    def __init__(self):
        pass

    def http_to_socks4(self, http_proxy):
        proxy_split = http_proxy.split(':')
        if len(proxy_split) != 2:
            return "Invalid HTTP proxy format. Please enter in the format 'IP:Port'."
        
        ip_address = proxy_split[0]
        port = int(proxy_split[1])

        socks4_proxy = f"{ip_address}:{port}"
        return socks4_proxy

    def http_to_socks5(self, http_proxy):
        proxy_split = http_proxy.split(':')
        if len(proxy_split) != 2:
            return "Invalid HTTP proxy format. Please enter in the format 'IP:Port'."
        
        ip_address = proxy_split[0]
        port = int(proxy_split[1])

        socks5_proxy = f"{ip_address}:{port}"
        return socks5_proxy

    def http_to_https(self, http_proxy):
        proxy_split = http_proxy.split(':')
        if len(proxy_split) != 2:
            return "Invalid HTTP proxy format. Please enter in the format 'IP:Port'."
        
        ip_address = proxy_split[0]
        port = int(proxy_split[1])

        https_proxy = f"{ip_address}:{port}"
        return https_proxy

    def convert_proxy(self, source_proxy, source_type, target_type):
        if source_type == 'HTTP':
            if target_type == 'SOCKS4':
                return self.http_to_socks4(source_proxy)
            elif target_type == 'SOCKS5':
                return self.http_to_socks5(source_proxy)
            elif target_type == 'HTTPS':
                return self.http_to_https(source_proxy)
            else:
                return "Target proxy format is not supported."

    def display_interface(self):
        print("Welcome to Proxy Converter!")
        source_proxy = input("Enter the proxy address to convert: ")
        source_type = input("Enter the source proxy format (HTTP, SOCKS4, SOCKS5, HTTPS): ")
        target_type = input("Enter the target proxy format (HTTP, SOCKS4, SOCKS5, HTTPS): ")
        result = self.convert_proxy(source_proxy, source_type.upper(), target_type.upper())
        print("Converted proxy address:", result)

    def handle_errors(self):
        pass

    def run(self):
        self.display_interface()
        self.handle_errors()

if __name__ == "__main__":
    converter = ProxyConverter()
    converter.run()