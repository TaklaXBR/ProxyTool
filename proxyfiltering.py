import speedtest
import requests
from bs4 import BeautifulSoup

class ProxyFiltering:
    def __init__(self):
        self.proxy_list = []

    def add_proxy(self):
        proxy = input("Enter proxy address (e.g., http://127.0.0.1:8080): ")
        self.proxy_list.append(proxy)
        print("Proxy added successfully.")

    def filter_by_speed(self, min_speed):
        """
        Filters the proxy list based on a minimum speed value.
        """
        filtered_proxies = []
        for proxy in self.proxy_list:
            speed = self.check_speed(proxy)
            if speed >= min_speed:
                filtered_proxies.append(proxy)
        return filtered_proxies

    def filter_by_anonymity(self, anonymity_level):
        """
        Filters the proxy list based on a specified anonymity level.
        """
        filtered_proxies = []
        for proxy in self.proxy_list:
            level = self.check_anonymity(proxy)
            if level == anonymity_level:
                filtered_proxies.append(proxy)
        return filtered_proxies

    def filter_by_country(self, country_code):
        """
        Filters the proxy list based on a specified country code.
        """
        filtered_proxies = []
        for proxy in self.proxy_list:
            code = self.check_country(proxy)
            if code == country_code:
                filtered_proxies.append(proxy)
        return filtered_proxies

    def check_speed(self, proxy):
        """
        Checks the speed of a specific proxy.
        """
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            st.download()
            speed = st.results.download / 1024 / 1024  
            return speed
        except Exception as e:
            print(f"An error occurred while checking proxy speed: {e}")
            return 0

    def check_anonymity(self, proxy):
        """
        Checks the anonymity level of a specific proxy.
        """
        try:
            response = requests.get("https://www.whatismyip.com/", proxies={"http": proxy, "https": proxy})
            soup = BeautifulSoup(response.text, "html.parser")
            anonymity_level = soup.find("span", class_="detLabel", string="Anonymity Level:").find_next_sibling("span").text.strip()
            return anonymity_level
        except Exception as e:
            print(f"An error occurred while checking anonymity level: {e}")
            return "Unknown"

    def check_country(self, proxy):
        """
        Checks the country code of a specific proxy.
        """
        try:
            response = requests.get("https://www.whatismyip.com/", proxies={"http": proxy, "https": proxy})
            soup = BeautifulSoup(response.text, "html.parser")
            country_code = soup.find("span", class_="detLabel", string="Country:").find_next_sibling("span").text.strip()
            return country_code
        except Exception as e:
            print(f"An error occurred while checking country code: {e}")
            return "Unknown"

    def display_proxies(self):
        for proxy in self.proxy_list:
            speed = self.check_speed(proxy)
            anonymity = self.check_anonymity(proxy)
            country = self.check_country(proxy)
            print(f"Proxy: {proxy}, Speed: {speed} Mbps, Anonymity: {anonymity}, Country: {country}")


proxy_filter = ProxyFiltering()
while True:
    print("1. Add Proxy")
    print("2. Filter Proxies by Speed")
    print("3. Filter Proxies by Anonymity Level")
    print("4. Filter Proxies by Country")
    print("5. Display Proxies")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        proxy_filter.add_proxy()
    elif choice == "2":
        min_speed = float(input("Enter minimum speed (Mbps): "))
        filtered_proxies = proxy_filter.filter_by_speed(min_speed)
        print("Filtered proxies by speed:")
        for proxy in filtered_proxies:
            print(proxy)
    elif choice == "3":
        anonymity_level = input("Enter anonymity level (e.g., Elite, Anonymous, Transparent): ")
        filtered_proxies = proxy_filter.filter_by_anonymity(anonymity_level)
        print(f"Filtered proxies by anonymity level ({anonymity_level}):")
        for proxy in filtered_proxies:
            print(proxy)
    elif choice == "4":
        country_code = input("Enter country code (e.g., US, CA, UK): ")
        filtered_proxies = proxy_filter.filter_by_country(country_code)
        print(f"Filtered proxies by country ({country_code}):")
        for proxy in filtered_proxies:
            print(proxy)
    elif choice == "5":
        print("All proxies:")
        proxy_filter.display_proxies()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")