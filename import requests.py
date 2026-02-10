import requests
from bs4 import BeautifulSoup
import csv
import os

# 1. SETUP - The URL we want to scrape
url = 'https://news.ycombinator.com/'

# 2. THE REQUEST - Get the raw HTML from the site
print("Connecting to Hacker News...")
try:
    response = requests.get(url)
    # Check if the website is actually working (Status 200 = OK)
    response.raise_for_status() 
except Exception as e:
    print(f"Error connecting to site: {e}")
    exit()

# 3. THE PARSER - Turn raw code into a searchable object
soup = BeautifulSoup(response.text, 'html.parser')
stories = soup.find_all('span', class_='titleline')

# 4. DATA COLLECTION & LOGIC - Filter for Python or AI
data_rows = []

for story in stories:
    title = story.getText()
    link = story.find('a')['href']
    
    # Using your 'LeetCode logic': Case-insensitive search
    # We use .lower() so we find 'AI', 'ai', 'Python', and 'python'
    if 'python' in title.lower() or 'ai' in title.lower():
        data_rows.append([title, link])

# 5. THE OUTPUT - Save to a CSV file
filename = 'scraped_news.csv'

# This ensures we find the file easily on your computer
file_path = os.path.join(os.getcwd(), filename)

with open(file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Write the column headers
    writer.writerow(['Title', 'URL'])
    # Write all the filtered stories
    writer.writerows(data_rows)

# 6. SUMMARY - Tell the user what happened
print("-" * 30)
print(f"SCRAPING COMPLETE!")
print(f"Found {len(data_rows)} stories related to Python or AI.")
print(f"Your file is saved here: {file_path}")
print("-" * 30)