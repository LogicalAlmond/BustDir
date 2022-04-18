import requests
import argparse

RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
RESET = '\u001b[0m'
VERSION = "0.1.0"
BANNER = '''
 ________  ___  ___  ________  _________  ________  ___  ________     
|\   __  \|\  \|\  \|\   ____\|\___   ___ \   ___ \|\  \|\   __  \    
\ \  \|\ /\ \  \ \  \ \  \___|\|___ \  \_\ \  \_|\ \ \  \ \  \|\  \   
 \ \   __  \ \  \ \  \ \_____  \   \ \  \ \ \  \  \ \ \  \ \   _  _\  
  \ \  \|\  \ \  \ \  \|____|\  \   \ \  \ \ \  \_ \ \ \  \ \   \  \| 
   \ \_______\ \_______\____\_\  \   \ \__\ \ \_______\ \__\ \__ \ _\ 
    \|_______|\|_______|\_________\   \|__|  \|_______|\|__|\|__|\|__|
                       \|_________|                                   
'''
print(BANNER)
print(f'[*] BustDir Version: {VERSION}')


def dirscan(domain):
    with open('Wordlists/directories.txt', 'r') as wordlist:
        for entry in wordlist:
            strippedEntry = entry.strip('\n')
            url = f'https://{domain}/{strippedEntry}'
            try:
                req = requests.get(url, allow_redirects=False)
                res = req.status_code
                if res == 200:
                    print(f'{GREEN}[+] {url}{RESET}')
                else:
                    print(f'{RED}[-] {url}{RESET}')
            except Exception as e:
                print(f'Error in request.')
                
                
if __name__ == "__main__":
    
    p = argparse.ArgumentParser()
    p.add_argument('-url', required=True, help='Url to scan')
    
    args = p.parse_args()
    url = args.url
    
    dirscan(url)