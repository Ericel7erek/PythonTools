import requests
from termcolor import colored

target_url = input('[+] Enter Target Url: ')
file_name = input('[+] Enter The Name Of The File Containing Directories: ')

def request(url):
	try:
		requests.get('http://' + url)
	except request.exceptions.ConnectionError:
		pass

file = open(file_name, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url + '/' + directory
	response = request(full_url)
	if response:
		print(colored(('[+] Directory Discovered At This Path: ' + full_url)))

