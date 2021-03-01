import requests

host, port = '127.0.0.1', 5000

# stop rest app
try:
    requests.get(f'http://{host}:{port}/stop_server')
except Exception as e:
    pass
finally:
    print("stop rest app")

