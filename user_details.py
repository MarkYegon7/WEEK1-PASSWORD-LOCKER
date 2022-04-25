import pyperclip
import random
import string


        
class Credentials:
    '''
    class to create account credentials,generate passwords and save information
    '''
    def __init__(self,user_name,site_name,account_name,password):
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
    credentials_list = []
    user_credential_list = []
        
    def save_credentials(self):
        Credentials.credentials_list.append(self)
        
    def generate_password():
        char=string.ascii_uppercase+string.ascii_lowercase+string.digits
        gen_pass=''.join(random.choice(char))
        return gen_pass
    
    @classmethod
    def display_credentials(cls,user_name):
        '''
        display list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return cls.credentials_list
    
    def find_by_site_name(cls, site_name):
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential
            
    def copy_credential(cls,site_name):
        find_credential = Credentials.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)