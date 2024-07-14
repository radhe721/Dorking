import webbrowser
import time

# List of search queries
search_queries = [
    'intitle:"Browse Directory"',
    'intitle:index.of',
    'intitle:"index of" database.properties',
    'intitle:"Index of" inurl:/parent-directory',
    'intitle:"Index of" inurl:/admin',
    'intitle:"Index of" inurl:/backup',
    'intitle:"Index of" inurl:/config',
    'intitle:"Index of" inurl:/logs',
    'intitle:"Admin Login"',
    'intitle:"Control Panel" inurl:/admin',
    'intitle:"Control Panel" inurl:/login',
    'filetype:pdf intitle:"Confidential"',
    'filetype:doc intitle:"Confidential"',
    'filetype:xls intitle:"Confidential"',
    'filetype:ppt intitle:"Confidential"',
    'intitle:login',
    'intitle:login inurl:/admin',
    'intitle:login inurl:/login',
    'inurl:login',
    'inurl:"/admin/login.php"',
    'site:preprod.* * inurl:login',
    'intext:"Powered by WordPress"',
    'intitle:"Login — WordPress"',
    'intitle:"powered by WordPress" version',
    'inurl:wp-content/plugins/',
    'inurl:/wp-content/plugins/revslider/'
]

# Function to generate Google search URLs with site:zomato.com
def generate_google_search_urls(queries, site):
    base_url = 'https://www.google.com/search?q='
    return [base_url + f"{query} site:{site}".replace(" ", "+") for query in queries]

# Generate URLs
print("Enter The Domain Name Here:", end="")
Domain_Name = input()
search_urls = generate_google_search_urls(search_queries, Domain_Name)

# Open URLs in batches of 5 in the default web browser
batch_size = 3
for i in range(0, len(search_urls), batch_size):
    batch = search_urls[i:i + batch_size]
    for url in batch:
        webbrowser.open(url)
    time.sleep(10)  # Wait 5 seconds before opening the next batch
