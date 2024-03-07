import requests
from bs4 import BeautifulSoup

def scrape_articles(url_file):
    # This python file follows the Single Responsibility Principle (SRP)
    # It only does the scraping of articles from the provided URLs.
    articles = []
    with open(url_file, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        response = requests.get(url.strip())
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text()
        
        # Find all paragraphs <p> content
        paragraphs = soup.find_all('p')
        content = '\n'.join([p.get_text() for p in paragraphs])

        articles.append({"title": title, "content": content})
    
    return articles