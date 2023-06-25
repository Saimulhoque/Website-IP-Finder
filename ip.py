import socket
from urllib.parse import urlparse

def get_ip_address(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except (socket.gaierror, ValueError):
        return None

# Example usage
url = ""
ip_address = get_ip_address(url)
if ip_address:
    print(f"The IP address of {url} is {ip_address}")
else:
    print(f"Failed to retrieve the IP address of {url}")
