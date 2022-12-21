import requests
import json


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
    user = dict()
    
    user['firstname'] = user_data['name']['first']
    user['lastname'] = user_data['name']['last']
    user['age'] = user_data['dob']['age']
    user['country'] = user_data['location']['country']

    return user


def get_users(url: str, n: int) -> list:
    '''get n users from url
    
    Args:
        url (str): api url
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    users = []
    while len(users) != n:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            user_data = data['results'][0]
            user = get_user(user_data)
            users.append(user)

    return users
    

def write_users_to_file(file_path: str, n: int):
    '''write n users to file

    Args:
        url (str): api url
        n (int): number of users
    '''
    users = get_users('https://randomuser.me/api/', n)
    with open(file_path, 'w') as f:
        data = json.dumps(users, indent=4)
        f.write(data)


write_users_to_file('data.json', 5)
