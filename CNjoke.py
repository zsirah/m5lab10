import requests

url = "http://api.icndb.com/jokes/random?limitTo=explicit"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
