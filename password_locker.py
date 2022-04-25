import pyperclip
from user_details import User, Credentials

def create_user(username,password):
    
    '''
   
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Save a new user account
    '''
    user.save_user()


def verify_user(username,password):
    '''
    verify user before creating credentials
    '''
    return User.check_user(username,password)
	 
def generate_password():
    '''
    Generates passwords
    '''
    return Credentials.generate_password()
	 
def create_credential(user_name,site_name,account_name,password):
    '''
    creates new credentials
    '''
    new_credential=Credentials(user_name,site_name,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    saves a newly created credential
    '''
    Credentials.save_credentials(credential)

def display_credentials(user_name):
	return Credentials.display_credentials(user_name)
	
def copy_credential(site_name):
    '''
    copy credential details to clipboard
    '''
    return Credentials.copy_credential(site_name)

def main():
	print(' ')
	print('Hello! Welcome to Paswaaad Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate:  acc-Create an Account , li-Log In , ex-Exit')
		short_code = input('Enter a choice: ')
		if short_code == 'ex':
			break

		elif short_code == 'acc':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			username = input('Enter your username - ')
			password = input('Enter your password - ')
			save_user(create_user(username,password))
			print(" ")
			print(f'New Account Created for:  {username} using password: {password}')
		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your user name - ')
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ')
						account_name = input('Enter your account\'s name - ')
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							option = input('Enter an option: ').lower()
							print("-"*60)
							if option == 'ep':
								print(" ")
								password = input('Enter your password: ')
								break
							elif option == 'gp':
								password = generate_password()
								break
							elif option == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')
				






if __name__ == '__main__':
	main()