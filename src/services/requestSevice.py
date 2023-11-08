import requests
import json

url = "localhost:5000/v1/register"


# curl --location 'localhost:5000/v1/register' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "username":"paulo@bnka.com",
#     "password":"Cluster.001"
# }'


payload = json.dumps({
  "username": "paulo@bnka.com",
  "password": "Cluster.001"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

