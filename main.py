import subprocess

def display_banner():
    banner = """
    ____        _   _                 
   / ___|  ___ | |_| |_ ___ _ __ ___  
   \___ \ / _ \| __| __/ _ \ '_ ` _ \ 
    ___) | (_) | |_| ||  __/ | | | | |
   |____/ \___/ \__|\__\___|_| |_| |_|
                                        
    """
    print(banner)

def main_menu():
    while True:
        display_banner()
        print("1. Proxy Checker")
        print("2. Proxy Finder")
        print("3. Proxy Speed Test")
        print("4. Proxy Reliability Test")
        print("5. Proxy Filtering")
        print("6. Proxy Automator")
        print("7. Port Scanner")
        print("8. Protocol Tester")
        print("9. Proxy Converter")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.run(['python', 'Proxychecker.py'])
        elif choice == '2':
            subprocess.run(['python', 'Proxyfinder.py'])
        elif choice == '3':
            subprocess.run(['python', 'ProxySpeedTest.py'])
        elif choice == '4':
            subprocess.run(['python', 'ProxyReliabilityTest.py'])
        elif choice == '5':
            subprocess.run(['python', 'proxyfiltering.py'])
        elif choice == '6':
            subprocess.run(['python', 'proxyautomator.py'])
        elif choice == '7':
            subprocess.run(['python', 'portscanner.py'])
        elif choice == '8':
            subprocess.run(['python', 'protocaltester.py'])
        elif choice == '9':
            subprocess.run(['python', 'proxyconverter.py'])
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()