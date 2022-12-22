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
    pass


def get_users(url: str, n: int) -> list:
    '''get n users from url
    
    Args:
        url (str): api url
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    pass
    

def write_users_to_file(file_path: str, n: int):
    '''write n users to file

    Args:
        url (str): api url
        n (int): number of users
    '''
    pass

