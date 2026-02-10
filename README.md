# 🕵️ Hacker News - AI & Python Monitor

A Python-based data automation tool that monitors Hacker News for specific tech trends. This project demonstrates web scraping, data filtering, and automated report generation.

## 🚀 How it Works
1. **Data Ingestion:** Uses `requests` to fetch real-time HTML from Hacker News.
2. **Parsing:** Uses `BeautifulSoup` to navigate the DOM and extract headlines and URLs.
3. **Logic Filter:** Applies a case-insensitive filter to isolate stories related to **AI** and **Python**.
4. **Export:** Generates a structured `scraped_news.csv` file for easy data analysis in Excel/Google Sheets.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** BeautifulSoup4, Requests, CSV
* **Logic:** String manipulation and conditional filtering.

## 📊 Sample Output
The script generates a CSV with the following structure:
| Title | URL |
| :--- | :--- |
| Why Python is king for AI | https://news.ycombinator.com/item?id=... |
| New AI model release | https://github.com/example/ai |

## ⚙️ Setup
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git`
2. Install dependencies: `pip install requests beautifulsoup4`
3. Run the script: `python hacker_news_scraper.py`