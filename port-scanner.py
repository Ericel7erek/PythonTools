import socket
import termcolor

def scan(target, ports):
    print(termcolor.colored('\n Scanning ' + str(target), 'green'))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1) 
        sock.connect((ipaddress, port))
        print(f'[+] Port {port} is Opened')
    except:
        pass
        # print(f'[-] Port {port} is Closed')  
    finally:
        sock.close() 

targets = input('[*] Enter Targets To Scan (split them by ,): ')
ports = int(input('[*] Enter How Many Ports You Want To Scan: '))

if ',' in targets:
    print('[*] Scanning Multiple Targets')
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)
