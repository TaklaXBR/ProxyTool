import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

def check_proxy(proxy):
    try:
        response = requests.get("http://example.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return True, response.elapsed.total_seconds() * 1000
    except Exception as e:
        pass
    return False, None

def main():
    proxy_file_path = input("Please enter the path of the proxy file: ")
    save_file = input("Do you want to save the working proxies to a file? (Y/N): ").lower().strip() == 'y'

    working_proxies = []
    not_working_proxies = []

    with open(proxy_file_path, 'r') as file:
        proxies = file.readlines()

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_proxy, proxies)

    for proxy, (is_working, ping) in zip(proxies, results):
        proxy = proxy.strip()
        if is_working:
            working_proxies.append((proxy, ping))
        else:
            not_working_proxies.append(proxy)

    print("Working Proxies:")
    for proxy, ping in working_proxies:
        print(f"{Fore.GREEN}{proxy} - Ping: {ping:.2f} ms{Style.RESET_ALL}")

    print("Not Working Proxies:")
    for proxy in not_working_proxies:
        print(f"{Fore.RED}{proxy}{Style.RESET_ALL}")

    if save_file:
        with open("working_proxies.txt", 'w') as file:
            for proxy, _ in working_proxies:
                file.write(proxy + '\n')

if __name__ == "__main__":
    main()