import requests
import time
import asyncio

async def test_proxy_speed(proxy):
    try:
        start_time = time.time()
        response = await asyncio.wait_for(requests.get("https://duckduckgo.com/", proxies={"http": proxy, "https": proxy}), timeout=10)
        end_time = time.time()
        if response.status_code == 200:
            speed = end_time - start_time
            return True, speed
    except Exception as e:
        pass
    return False, None

async def test_multiple_proxies(proxies):
    results = []
    for proxy in proxies:
        is_working, speed = await test_proxy_speed(proxy)
        if is_working:
            results.append((proxy, speed))
    return results

def filter_proxies_by_speed(proxies, threshold):
    return [proxy for proxy in proxies if proxy[1] is not None and proxy[1] >= threshold]

def get_proxies_from_user():
    proxies = []
    while True:
        proxy = input("Please enter a proxy (or press Enter to finish): ").strip()
        if not proxy:
            break
        proxies.append(proxy)
    return proxies

async def main():
    proxies = get_proxies_from_user()
    if not proxies:
        print("No proxies provided. Exiting.")
        return []

    if not all(proxy.startswith("http") for proxy in proxies):
        print("Invalid proxy format. Proxy addresses should start with 'http'.")
        return []

    if not all(proxy.startswith("http://") or proxy.startswith("https://") for proxy in proxies):
        print("Invalid proxy format. Proxy addresses should start with 'http://' or 'https://'.")
        return []

    try:
        results = await asyncio.wait_for(test_multiple_proxies(proxies), timeout=10)
    except asyncio.TimeoutError:
        print("Timeout: Proxy testing took too long.")
        return []

    print("Test results:")
    for proxy, speed in results:
        print(f"Proxy: {proxy}, Speed: {speed}")

    if not results:
        print("No working proxies found.")
    else:
        print("Working proxies found.")
    
    return results

if __name__ == "__main__":
    asyncio.run(main())