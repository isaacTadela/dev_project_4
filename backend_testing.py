import requests


id, user_name = 15, "dan15"

host, port = 'localhost', 5000

    
try:
    res = requests.get(f'http://{host}:{port}')
    print("get response for home page -", res.text)
    
    res = requests.get(f'http://{host}:{port}/users/{id}')
    print("get response for id=15 -", res.text)

    res = requests.get(f'http://{host}:{port}/users/58')
    print("get response for nobady -", res.text)

except Exception as e:
    print("test failed", e)
    raise Exception(e)
