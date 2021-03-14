import requests


id = 1

with open("k8s_url.txt", "r") as f:
    lines = f.read().splitlines()

for line in lines:
    if line.startswith("http"):
        url = line
        break

print(url)

try:
    print(f'{url}')

    res = requests.get(f'{url}')
    print("get response for home page -", res.text)

    res = requests.get(f'{url}/users/{id}')
    print("get response for user id = 1 -", res.json())
except Exception as e:
    print("test failed", e)
    raise Exception(e)