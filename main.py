```python
import requests
from bs4 import BeautifulSoup
import argparse

def fetch_ip_info(ip_address):
    """
    Fetches information about a given IP address using an online API.
    
    Args:
        ip_address (str): The IP address to query.
    
    Returns:
        dict: Parsed JSON response containing IP information.
    """
    try:
        # API endpoint for IP geolocation
        url = f'https://ipinfo.io/{ip_address}/json'
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for {ip_address}: {e}")
        return None

def display_info(ip_info):
    """
    Displays the information retrieved for an IP address.
    
    Args:
        ip_info (dict): The information about the IP address.
    """
    if ip_info:
        print(f"IP Address: {ip_info.get('ip')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
    else:
        print("No information available.")

def main():
    # Setting up argument parsing for command line usage
    parser = argparse.ArgumentParser(description='Fetch IP address information.')
    parser.add_argument('ip', type=str, help='IP address to lookup')
    args = parser.parse_args()

    # Fetch and display IP information
    ip_info = fetch_ip_info(args.ip)
    display_info(ip_info)

if __name__ == "__main__":
    main()
```