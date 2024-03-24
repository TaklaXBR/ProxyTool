import requests
import time

class ProxyAutomator:
    def __init__(self):
        self.proxy_list = []

    def display_menu(self):
        print("1. Add Proxy")
        print("2. Remove Proxy")
        print("3. Run Auto Update")
        print("4. Exit")

    def add_proxy(self):
        proxy = input("Enter proxy address (e.g., http://127.0.0.1:8080): ")
        self.proxy_list.append(proxy)
        print("Proxy added successfully.")

    def remove_proxy(self):
        if not self.proxy_list:
            print("No proxies added yet.")
            return
        print("Current proxies:")
        for i, proxy in enumerate(self.proxy_list):
            print(f"{i + 1}. {proxy}")
        index = int(input("Enter the index of the proxy to remove: ")) - 1
        if 0 <= index < len(self.proxy_list):
            del self.proxy_list[index]
            print("Proxy removed successfully.")
        else:
            print("Invalid index.")

    def check_proxy(self, proxy):
        try:
            response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
            if response.status_code == 200:
                return True
        except Exception as e:
            pass
        return False

    def update_proxy_list(self):
        updated_list = []
        for proxy in self.proxy_list:
            if self.check_proxy(proxy):
                updated_list.append(proxy)
        self.proxy_list = updated_list

    def run_auto_update(self, interval):
        while True:
            self.update_proxy_list()
            print("Proxy list updated at", time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(interval)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_proxy()
            elif choice == '2':
                self.remove_proxy()
            elif choice == '3':
                interval = int(input("Enter auto update interval (in seconds): "))
                self.run_auto_update(interval)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    proxy_automator = ProxyAutomator()
    proxy_automator.run()