import time
import requests
import random
import urllib.parse
import os
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m-------------[XKucoin Bot]-------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def read_data_file(file_path):
    accounts = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            encoded_data = line.strip()
            if encoded_data:
                accounts.append(encoded_data)
    return accounts

def decode_data(encoded_data):
    params = dict(item.split('=') for item in encoded_data.split('&'))

    decoded_user = urllib.parse.unquote(params['user'])
    decoded_start_param = urllib.parse.unquote(params['start_param'])

    return {
        "decoded_user": decoded_user,
        "decoded_start_param": decoded_start_param,
        "hash": params['hash'],
        "auth_date": params['auth_date'],
        "chat_type": params['chat_type'],
        "chat_instance": params['chat_instance']
    }

def login(decoded_data):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/login?lang=en_US"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-request-with": "null",
        "Referer": "https://www.kucoin.com/miniapp/tap-game?inviterUserId=7297908766&rcode=QP3W3339"
    }
    
    body = {
        "inviterUserId": "7297908766",
        "extInfo": {
            "hash": decoded_data['hash'],
            "auth_date": decoded_data['auth_date'],
            "via": "miniApp",
            "user": decoded_data['decoded_user'],
            "chat_type": decoded_data['chat_type'],
            "chat_instance": decoded_data['chat_instance'],
            "start_param": decoded_data['decoded_start_param']
        }
    }

    session = requests.Session()
    response = session.post(url, headers=headers, json=body)
    cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in session.cookies])             
    return cookie

def data(cookie):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/summary?lang=en_US"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-request-with": "null",
        "Referer": "https://www.kucoin.com/miniapp/tap-game?inviterUserId=7297908766&rcode=QP3W3339",
        "cookie": cookie
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    balance = data.get("data").get("availableAmount")
    molecule = data.get("data").get("feedPreview").get("molecule")
    print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance}")
    return molecule

def tap(cookie, molecule):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/gold/increase?lang=en_US"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-request-with": "null",
        "Referer": "https://www.kucoin.com/miniapp/tap-game?inviterUserId=7297908766&rcode=QP3W3339",
        "cookie": cookie
    }

    total_increment = 0
    max_taps = random.randint(50, 60)  # Limit taps to avoid flood

    while total_increment < 3000 and max_taps > 0:
        increment = random.randint(55, 60)  # Randomize increment value each iteration
        form_data = {
            'increment': str(increment),
            'molecule': str(molecule)
        }

        response = requests.post(url, headers=headers, data=form_data)
        total_increment += increment
        
        colors = [Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.RED]
        random_color = random.choice(colors)
        print(f"{random_color}{Style.BRIGHT}Tapped: {Fore.WHITE + Style.BRIGHT}{increment} | {random_color}Total Tap: {Fore.WHITE + Style.BRIGHT}{total_increment}/3000 {Style.RESET_ALL}")
        
        max_taps -= 1
        time.sleep(random.randint(3, 7))  # Random delay between taps to prevent flooding

def new_balance(cookie):
    url = "https://www.kucoin.com/_api/xkucoin/platform-telebot/game/summary?lang=en_US"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-request-with": "null",
        "Referer": "https://www.kucoin.com/miniapp/tap-game?inviterUserId=7297908766&rcode=QP3W3339",
        "cookie": cookie
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    balance = data.get("data").get("availableAmount")
    print(f"{Fore.CYAN + Style.BRIGHT}New Balance: {Fore.WHITE + Style.BRIGHT}{balance}")

def process_account(encoded_data):
    decoded_data = decode_data(encoded_data)
    cookie = login(decoded_data)
    molecule = data(cookie)
    tap(cookie, molecule)
    new_balance(cookie)

def main():
    file_path = "data.txt"
    while True:
        accounts = read_data_file(file_path)

        clear_terminal()
        art()

        with ThreadPoolExecutor() as executor:
            executor.map(process_account, accounts)
        
        print(f"{Fore.YELLOW}Waiting for 5 minutes before the next loop...")
        countdown_timer(300)  # Wait for 30 minutes before starting again

if __name__ == "__main__":
    main()
