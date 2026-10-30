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
- Books scraped: 1,000 across 50 genres, with no bad price values
- Average price: £35.07
- Rating vs. price: almost no relationship. One-star books average £34.56 and five-star books £35.37.
- Most and least expensive genres: this needs care. Taken literally, the top genre is Suspense (£58.33) and the cheapest is Crime (£10.97), but each of those has only one book, so the “average” is just one price. If you only count genres with 10 or more books:
  - Most expensive: Travel (£39.79, 11 books), then Fantasy (£39.59, 48 books)
  - Cheapest: Food and Drink (£31.41, 30 books), then Thriller and Mystery

## How to run
pip install requests beautifulsoup4 pandas
python book_tracker.py
