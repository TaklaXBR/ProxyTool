import requests

class ProxyReliabilityTest:
    def test_proxy_reliability(self, proxy):
        try:
            
            response = requests.get("https://www.wikipedia.org", proxies={"http": proxy}, timeout=15)
            if response.status_code == 200:
                
                response = requests.get("https://www.wikipedia.org", proxies={"https": proxy}, timeout=15)
                if response.status_code == 200:
                    
                    return True
        except Exception as e:
            print(f"Error occurred while testing proxy {proxy}: {e}")
        return False

    def test_multiple_proxies(self, proxies):
        reliable_proxies = []
        for proxy in proxies:
            if self.test_proxy_reliability(proxy):
                reliable_proxies.append(proxy)
        return reliable_proxies

    def get_user_proxies(self):
        proxies = []
        while True:
            proxy = input("Please enter a proxy (or press Enter to finish): ").strip()
            if not proxy:
                break
            proxies.append(proxy)
        return proxies

    def save_to_file(self, proxies, filename):
        with open(filename, 'w') as file:
            for proxy in proxies:
                file.write(proxy + '\n')

    def main(self):
        proxies = self.get_user_proxies()
        if not proxies:
            print("No proxies provided. Exiting.")
            return

        reliable_proxies = self.test_multiple_proxies(proxies)

        if not reliable_proxies:
            print("No reliable proxies found.")
            return

        print("Reliable proxies:")
        for proxy in reliable_proxies:
            print(f"- {proxy}")

        self.save_to_file(reliable_proxies, "safeproxy.txt")
        print("Reliable proxies saved to safeproxy.txt")

if __name__ == "__main__":
    proxy_test = ProxyReliabilityTest()
    proxy_test.main()