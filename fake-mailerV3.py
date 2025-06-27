import os
import sys
import time
import requests

# التحقق من الاتصال بالإنترنت
try:
    requests.get("https://www.google.com", timeout=3)
except (requests.ConnectionError, requests.Timeout):
    print("[!] No internet connection [!]")
    sys.exit()

# ألوان الطرفية
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)

logo = """
\033[1;32m    ___    ____  __  __       _       _           
\033[1;32m   / _ |  / __ \|  \/  |     (_)     | |          
\033[1;32m  / __ | | |  | | \  / | __ _ _ _ __ | |__  _   _ 
\033[1;32m / /_| |_| |  | | |\/| |/ _` | | '_ \| '_ \| | | |
\033[1;32m \___/(_) _|  |_|_|  |_|\__,_|_| .__/|_.__/ \__, |
\033[1;32m                               | |           __/ |
\033[1;32m                               |_|          |___/ 

\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m DEVELOPED BY \033[1;33mABDevlopers
"""

os.system("clear")
print(logo)
hprint(G + 'Launching Fake Mailer...')
time.sleep(1)

# جمع معلومات البريد
to = input(G + "Send Mail To" + C + " : " + Y)
subject = input(G + "Input Mail Subject" + C + " : " + Y)
msg = input(G + "Input Mail Content" + C + " : " + Y)

# إعدادات HTTP
headers = {
    'Host': 'anonymouse.org',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 '
                  'Chrome/85.0.4183.101 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://anonymouse.org/anonemail.html',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'to': to,
    'subject': subject,
    'text': msg
}

# إرسال البريد
try:
    response = requests.post("http://anonymouse.org/cgi-bin/anon-email.cgi", headers=headers, data=data)
    if response.ok:
        hprint(G + "Sending Email >>>>>>>>>>")
        time.sleep(2)
        hprint(C + "Mail Successfully Sent!!")
        time.sleep(1)
        hprint(W + "Process can take some time!!")
        print()
        print(Y + "Visit www.github.com/htr-tech for More Tools" + W)
    else:
        hprint(R + "Failed to send email. Server responded with status code: " + str(response.status_code))
except Exception as e:
    hprint(R + f"An error occurred: {e}")
