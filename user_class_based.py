import requests



class RandomUser:
    def __init__(self) -> None:
        self.url = 'https://randomuser.me/api/'
        self.response = requests.get(self.url)
        
    def get_randomuser(self) -> dict:
        '''get full data from randomuser
        
        Returns:
            dict: full data
        '''
        data = self.response.json()
        return data
    
    def get_cell(self) -> str:
        '''get user cell from randomuser
        
        Returns:
            str: user cell
        '''
        return self.response.text
    
    def get_city(self) -> str:
        '''get user city from randomuser
        
        Returns:
            str: user city
        '''
        data = self.response.json()
        user_city = data['results'][0]['location']['city']
        return user_city
    
    def get_dob(self) -> dict:
        '''get user dob from randomuser
        
        Returns:
            dict: user dob
        '''
        data = randomuser.get_randomuser()
        return data['results'][0]['dob']
    
    def get_email(self) -> str:
        '''get user email from randomuser
        
        Returns:
            str: user email
        '''
        data = randomuser.get_randomuser()
        return data['results'][0]['email']

    def get_first_name(self) -> str:
        '''get user first name from randomuser
        
        Returns:
            str: user first name
        '''
        data = randomuser.get_randomuser()
        return data['results'][0]['name']['first']

    def get_last_name(self) -> str:
        '''get user last name from randomuser
        
        Returns:
            str: user last name
        '''
        data = randomuser.get_randomuser()
        return data['results'][0]['name']['last']

    def get_full_name(self) -> str:
        '''get user full name from randomuser
        
        Returns:
            str: user full name
        '''
        data = randomuser.get_randomuser()
        return data['results'][0]['name']

    def get_gender(self) -> str:
        '''get user gender from randomuser
        
        Returns:
            str: user gender
        '''
        data = randomuser.get_randomuser()
        return data['results'][0]['gender']
    
    def get_id(self) -> dict:
        '''get user id from randomuser
        
        Returns:
            dict: user id
        '''
        data = randomuser.get_randomuser()
        return data['results'][0]['id']
    
    def get_id_number(self) -> str:
        '''get user id number from randomuser
        
        Returns:
            str: user id number
        '''
        return randomuser.get_id()['value']
    
    def get_info(self) -> dict:
        '''get user info from randomuser
        
        Returns:
            dict: user info
        '''
        data = randomuser.get_randomuser()
        return data['info']
    
    def get_nat(self) -> str:
        '''get user nat from randomuser
        
        Returns:
            str: user nat
        '''
        return randomuser.get_randomuser()['results'][0]['nat']
    
    def get_picture(self) -> dict:
        '''get user picture from randomuser
        
        Returns:
            dict: user picture
        '''
        return randomuser.get_randomuser()['results'][0]['picture']

randomuser = RandomUser()

# print(randomuser.get_randomuser())
# print(randomuser.get_cell())
# print(randomuser.get_city())
print(randomuser.get_dob())
print(randomuser.get_email())
print(randomuser.get_first_name())
print(randomuser.get_last_name())
print(randomuser.get_full_name())
print(randomuser.get_gender())
print(randomuser.get_id())
print(randomuser.get_id_number())
print(randomuser.get_info())
print(randomuser.get_nat())
print(randomuser.get_picture())
