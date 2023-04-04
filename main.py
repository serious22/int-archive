import requests
import re

# Define the URL for the Wikipedia API
url = 'https://en.wikipedia.org/w/api.php'

# Set the parameters for the API request
params = {
    'action': 'query',
    'prop': 'revisions',
    'titles': 'Python (programming language)',
    'rvprop': 'content',
    'rvslots': '*',
    'format': 'json'
}

# Make the API request
response = requests.get(url, params=params).json()

# Extract the page content from the API response
page_id = list(response['query']['pages'].keys())[0]
page_content = response['query']['pages'][page_id]['revisions'][0]['slots']['main']['*']

ref_pattern = r'<ref.*?</ref>'

references = re.findall(ref_pattern, page_content, re.DOTALL)

# Extract metadata for each reference
for ref in references:
   
    url_pattern = r'url\s*=\s*(.*?)\s*\|'
    author_pattern = r'author\s*=\s*(.*?)\s*\|'
    date_pattern = r'date\s*=\s*(.*?)\s*\|'

    url = re.search(url_pattern, ref).group(1)
    date = re.search(date_pattern, ref).group(1)

    print(f'URL: {url}')
    print(f'Date: {date}')
