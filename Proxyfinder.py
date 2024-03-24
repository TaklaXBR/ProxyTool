import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def find_proxies(url):
    proxies = []

    
    response = requests.get(url)
    
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    
    proxy_table = soup.find('tbody')
    if proxy_table:
        proxy_list = proxy_table.find_all('tr')

        
        for row in proxy_list:
            columns = row.find_all('td')
            proxy = f"{columns[0].text.strip()}:{columns[1].text.strip()}"
            proxies.append(proxy)

    return proxies

def save_proxies(proxies, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for proxy in proxies:
            file.write(proxy + '\n')

def main():
    url = input("Please enter the URL to fetch proxies from: ").strip()
    proxies = find_proxies(url)

    
    with open("custom_proxies.txt", 'w', encoding='utf-8') as file:
        print(f"Found {len(proxies)} proxies from {url}:")
        for proxy in proxies:
            print(f"{Fore.GREEN}{proxy}{Style.RESET_ALL}")
            file.write(proxy + '\n')

if __name__ == "__main__":
    main()