```python
import requests
from bs4 import BeautifulSoup
import whois

# Function to perform a basic DNS lookup using the whois library
def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        print(f"Error retrieving WHOIS info: {e}")
        return None

# Function to scrape the title of a webpage
def scrape_webpage_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        return title
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Main function to execute the OSINT tasks
def main():
    domain = input("Enter a domain (e.g., example.com): ")
    
    # Get WHOIS information
    print(f"\nRetrieving WHOIS info for {domain}...")
    domain_info = get_domain_info(domain)
    if domain_info:
        print("WHOIS Information:")
        print(domain_info)

    # Get website title
    url = f"http://{domain}"
    print(f"\nFetching title for {url}...")
    title = scrape_webpage_title(url)
    if title:
        print(f"Title of the webpage: {title}")

if __name__ == "__main__":
    main()
```
