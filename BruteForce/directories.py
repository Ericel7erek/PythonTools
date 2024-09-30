import requests
from termcolor import colored

target_url = input('[+] Enter The Targeted Url: ')
file_name = input('[+] Enter The Name Of The File Containing Directories: ')

def request(url):
	try:
		return requests.get('http://'+ url)
	except requests.exceptions.ConnectionError:
		pass

file = open(file_name, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url + '/' + directory
	response = request(full_url)
	if response:
		print(colored(('[+] Discovered Directory At This Path ' + full_url), 'green'))
