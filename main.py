from pystyle import Colors, Colorate
import os
import random
import requests
import re
import time
from requests.exceptions import RequestException
from concurrent.futures import ThreadPoolExecutor, as_completed

os.system('cls')

def check_proxy(proxy):
    try:
        response = requests.get('http://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return proxy
    except RequestException:
        return None

menu_text = r"""     
                                     

                                          ____  __ __  _____ ______  ____  _____  __ __ 
                                         |    ||  |  |/ ___/|      ||    ||     ||  |  |
                                         |__  ||  |  (   \_ |      | |  | |   __||  |  |
                                         __|  ||  |  |\__  ||_|  |_| |  | |  |_  |  ~  |
                                        /  |  ||  :  |/  \ |  |  |   |  | |   _] |___, |
                                        \  `  ||     |\    |  |  |   |  | |  |   |     |
                                         \____| \__,_| \___|  |__|  |____||__|   |____/ 
                                                
                                        
                                     ╔══════════════════════════════════════════════════════╗
                                     ║                                                      ║
                                     ║      [1] Https      [2] Socks4      [3] Socks5       ║
                                     ║                                                      ║
                                     ╚══════════════════════════════════════════════════════╝ 
                        
"""
print(Colorate.Horizontal(Colors.blue_to_white, menu_text,1))
option = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] > ', 1))
if option == "1": #HTPPS
    https = [
        "https://spys.me/proxy.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt"
    ]
    proxies = set()
    valid_proxies = []
    for proxy in https:
        r = requests.get(proxy)
        valid_proxies = re.findall(r'http[s]?://([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+)', r.text)
        proxies.update(valid_proxies)

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_proxy, proxy): proxy for proxy in proxies}
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                valid_proxies.append(result)
                print(Colorate.Horizontal(Colors.green_to_white, f"                                     [@] > VALID | {result}",1))
                
            else:
                fakeip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":80" # makes the checker look better does nothing!
                print(Colorate.Horizontal(Colors.red_to_white, f"                                     [@] > INVALID | {fakeip}",1))

    for proxy in valid_proxies:
        with open("proxies.txt", "w") as file:
                 file.write(f"{result}")
                 file.write(f"\n")
    time.sleep(1)
    line_count = len(valid_proxies)
    print(Colorate.Horizontal(Colors.blue_to_white, f"                                     [@] > SCRAPED | HTTPS | {line_count}",1))

if option == "2":
    socks4 = [
        "https://socks-proxy.net/",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt"
    ]
    proxies = set()
    valid_proxies = []
    for proxy in socks4:
        r = requests.get(proxy)
        valid_proxies = re.findall(r'http[s]?://([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+)', r.text)
        proxies.update(valid_proxies)
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_proxy, proxy): proxy for proxy in proxies}
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                valid_proxies.append(result)
                print(Colorate.Horizontal(Colors.green_to_white, f"                                     [@] > VALID | {result}",1))
                
            else:
                fakeip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":80" # makes the checker look better does nothing!
                print(Colorate.Horizontal(Colors.red_to_white, f"                                     [@] > INVALID | {fakeip}",1))

    for proxy in valid_proxies:
        with open("proxies.txt", "w") as file:
                 file.write(f"{result}")
                 file.write(f"\n")

    time.sleep(1)
    line_count = len(valid_proxies)
    print(Colorate.Horizontal(Colors.blue_to_white, f"                                     [@] > SCRAPED | SOCKS4 | {line_count}",1))

if option == "3":
    socks5 = [
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt"
    ]
    proxies = set()
    valid_proxies = []
    for proxy in socks5:
        r = requests.get(proxy)
        valid_proxies = re.findall(r'http[s]?://([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+)', r.text)
        proxies.update(valid_proxies)
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_proxy, proxy): proxy for proxy in proxies}
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                valid_proxies.append(result)
                print(Colorate.Horizontal(Colors.green_to_white, f"                                     [@] > VALID | {result}",1))
            else:
                fakeip = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + ":80" # makes the checker look better does nothing!
                print(Colorate.Horizontal(Colors.red_to_white, f"                                     [@] > INVALID | {fakeip}",1))

    for proxy in valid_proxies:
        with open("proxies.txt", "w") as file:
                 file.write(f"{result}")
                 file.write(f"\n")
                 
    time.sleep(1)
    line_count = len(valid_proxies)
    print(Colorate.Horizontal(Colors.blue_to_white, f"                                     [@] > SCRAPED | SOCKS5 | {line_count}",1))
