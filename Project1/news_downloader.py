import requests
from bs4 import BeautifulSoup
import os

#get the news articles in order to scrap them using / read files
with open('url.txt','r') as file:
    urls = file.readlines()

    #create a directory to put the files
if not os.path.exists('articles'):
    os.makedirs('articles')


       #go through all of the articles and strip them
for url in urls:
    url = url.strip()

        #parsing the article using the beautiful soup library in my environment, varible soup
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
     
        
        #gwt the title
    title = soup.find('title').get_text()
    content = ''

#for output style purpose add new lines
#iterate over each element to get title and paragraphs
#find paragraphs using p element
#find all headers using an array of headers
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for header in headers:
        content += f'\n{header.get_text()}\n'
        paragraph = header.find_next_sibling('p')
        while paragraph:
            content += paragraph.get_text() + '\n'
            paragraph = paragraph.find_next_sibling('p')

    # Write content to a file in srticles directory
    file_name = f'articles/{title}.txt'
    with open(file_name, 'w') as article_file:
        article_file.write(content)

    # Print the downloaded files
    print(f'Article downloaded: {title}')
    

