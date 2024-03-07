import socket

def resolve_To_ip(domain):
    try :
        ip_address = socket.gethostbyname(domain)
        return ip_address

    except socket.gaierror as e :
        return none

if __name__ == "__main__":
    domain = input("Enter The Domain Name: ")
    ip_address = resolve_To_ip(domain)

    if ip_address :
        print(f"The Ip address of {domain}  is: {ip_address}")
    else :
        print(f"Failed to resolve {domain} to IP address")


