import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth

load_dotenv()

DOMAIN=os.getenv("DOMAIN")
LOGIN=os.getenv("LOGIN")
PASSWORD=os.getenv("PASSWORD")

result = requests.get('https://api.ipify.org')
if result.ok:
    IP = result.text
    result = requests.get('https://www.ovh.com/nic/update?system=dyndns&hostname=%s&myip=%s' % (DOMAIN, IP), auth=HTTPBasicAuth(LOGIN, PASSWORD))
    print(result.text)
else:
    print("Failed to get current public IP")