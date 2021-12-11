import socket
from IPy import IP


def scan_port(ipaddress, port):
    # condition to test for open ports
    try:
        # create socket
        sock = socket.socket()
        # set a timeout on the socket so it doesn't stall while running
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print(f'[+] Port ' + str(port) + ' is Open')
    # catches all closed ports
    except:
        print(f'[-] Port ' + str(port) + ' is Closed')

# enter the ip address to scan
ipaddress = input('[+] Enter Target to Scan: ')

# iterate range of ports to scan
for port in range(75, 85):
    scan_port(ipaddress, port)
