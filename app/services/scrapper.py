import requests
from bs4 import BeautifulSoup

async def scrape_linkedin_page(page_id: str):
    url = f"https://www.linkedin.com/company/{page_id}/"
    
    #add more stuff here dumboo
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #extracting name and stufff
    name = soup.find('h1', class_='org-top-card-summary__title').text.strip()
    description = soup.find('p', class_='org-top-card-summary__tagline').text.strip()
    
    
    return {
        "page_id": page_id,
        "name": name,
        "description": description,
    }