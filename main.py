'''test requests'''
import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print('some request errors')