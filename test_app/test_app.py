import json

from pprint import pprint
import requests

port = "5000"
ip_addrs = [
    "http://localhost"
]

for ip_addr in ip_addrs:
    try:        
        url = f"{ip_addr}:{port}"
        resp = requests.get(url)
        print(f"ip_addr: {ip_addr} succeeded")
        print(resp.text)        

        data = {"key": "12345", "value": "Christopher"}

        resp = requests.post(f"{url}/addData", json=(data))
        
        print(resp.text)

    except Exception as e:
        print(f"ip_addr: {ip_addr} failed")
