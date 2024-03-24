import requests

class ProxyProtocolTester:
    def __init__(self):
        pass

    def test_proxy(self, proxy_list):
        protocols = ['HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5']
        for proxy in proxy_list:
            print(f"\nTesting proxy: {proxy}")
            for protocol in protocols:
                proxy_dict = {protocol.lower(): proxy}
                try:
                    response = requests.get('https://httpbin.org/ip', proxies=proxy_dict, timeout=5)
                    if response.status_code == 200:
                        print(f"{protocol}: True")
                    else:
                        print(f"{protocol}: False")
                except Exception as e:
                    print(f"{protocol}: False")

    def display_interface(self):
        print("Welcome to Proxy Protocol Tester!")
        proxy_input = input("Enter proxy addresses separated by commas (e.g., proxy1:port,proxy2:port): ")
        proxy_list = [p.strip() for p in proxy_input.split(',')]
        self.test_proxy(proxy_list)

    def run(self):
        self.display_interface()

if __name__ == "__main__":
    tester = ProxyProtocolTester()
    tester.run()