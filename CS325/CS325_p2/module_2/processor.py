import os
from datetime import datetime

def sanitize_filename(filename):
    # This python file follows the Open Closed Principle (OCP)
    # It is open for extensions and closed for modification.
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '_')]).rstrip()

# processed and saves the articles
def process_and_save_article(article, url_or_path):
    raw_directory = "Data/raw/"
    processed_directory = "Data/processed/"
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    raw_filename = f"{timestamp}_raw.txt"  # For example purposes
    processed_filename = f"{sanitize_filename(article['title'])}.txt"

    if not os.path.exists(raw_directory):
        os.makedirs(raw_directory)
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)

    # Write the actual article content to the raw file
    with open(os.path.join(raw_directory, raw_filename), 'w') as raw_file:
        raw_file.write(article['content'])

    # Saving the data once its been processed
    with open(os.path.join(processed_directory, processed_filename), 'w') as processed_file:
        processed_file.write(article['content'])  # You may want to write something else here

    print(f"Article processed and saved: {processed_filename}")