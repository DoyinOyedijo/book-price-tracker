# Book Price Tracker

A Python web scraper that collects data on all 1000 books from 
[books.toscrape.com](https://books.toscrape.com) and performs 
pricing analysis by genre and rating.

## What it does
- Scrapes all 50 genres and their books automatically
- Collects title, price, rating, availability, and genre
- Cleans and analyzes data using pandas
- Exports results to CSV

## Technologies
- Python
- BeautifulSoup4
- Requests
- Pandas

## Key findings
- Total books scraped: 1000
- Average book price: £X.XX
- Most expensive genre: X
- Cheapest genre: X

## How to run
pip install requests beautifulsoup4 pandas
python book_tracker.py
