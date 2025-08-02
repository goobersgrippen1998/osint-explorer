```python
import requests
import json

def fetch_ip_info(ip_address):
    """
    Fetches information about an IP address using the ipinfo.io API.
    
    Parameters:
        ip_address (str): The IP address to look up.
        
    Returns:
        dict: A dictionary containing the IP information.
    """
    try:
        # API endpoint for fetching IP information
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for {ip_address}: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_ip_info(ip_info):
    """
    Displays the IP information in a readable format.
    
    Parameters:
        ip_info (dict): The dictionary containing IP information.
    """
    if ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No information available.")

def main():
    """
    Main function to run the OSINT IP information script.
    Prompts the user for an IP address and displays the information.
    """
    ip_address = input("Enter an IP address to lookup: ")
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```