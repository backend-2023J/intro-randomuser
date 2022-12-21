# randomuser

intorduction to requests and working with api

## install requests
```bash
pip install requests
```

## test request module

`/main.py` - import module
```python
import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print('some request errors')
```

## user
`/user.py` - import module
```python
import requests
import json
```

`/user.py` - get_user()
```python
def get_user(user_data: dict) -> dict:
    '''get user from data
    
    Args:
        user_data (dict): user data from https://randomuser.me/api/
        
    Returns:
        dict: {
            'firstname': user firstname,
            'lastname': user lastname,
            'age': user age,
            'country': user country
        }
    '''
    pass
```

`/user.py` - get_users()
```python
def get_users(url: str, n: int) -> list:
    '''get n users from url
    
    Args:
        url (str): api url
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    pass
```

`/user.py` - write_users_to_file()
```python
def write_users_to_file(file_path: str, n: int):
    '''write n users to file

    Args:
        url (str): api url
        n (int): number of users
    '''
    pass

```

`/data.json` - file
```python
[
    {
        "firstname": "Delmar",
        "lastname": "Viana",
        "age": 73,
        "country": "Brazil"
    },
    {
        "firstname": "Zdravko",
        "lastname": "Vuji\u010di\u0107",
        "age": 51,
        "country": "Serbia"
    },
    ...
    ,
]
```