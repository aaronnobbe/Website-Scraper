import sys
from module_1.scraper import scrape_articles
from module_2.processor import process_and_save_article

def main():
    # Check if the URL_FILE argument is provided
    if len(sys.argv) < 2:
        print("Usage: python run.py <URL_FILE>")
        sys.exit(1)

    # Extract the URL_FILE argument from command line
    url_file = sys.argv[1]
    
    # Scrape articles from the URLs in the URL_FILE
    articles = scrape_articles(url_file)

    # Process and save each article
    for article in articles:
        process_and_save_article(article, url_file)

if __name__ == "__main__":
    main()