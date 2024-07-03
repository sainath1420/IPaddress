import socket


def get_hostname_ip():
    hostname = input("Please enter a website address (URL): ")
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f'Hostname: {hostname}')
        print(f'IP: {ip_address}')
    except socket.gaierror as error:
        print(f'Invalid hostname or address, error: {error}')


get_hostname_ip()
