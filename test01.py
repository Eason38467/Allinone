import requests
import json

username = 'admin'
password = 'cisco!123'
mgmt = '192.168.51.31'

myhead = {'content-type': 'application/json'}

url = "http://" + mgmt + "/ins"

payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",

    }
}

response = requests.post(url,data=payload,verify=False,auth=(username,password)).json()

print(response)
