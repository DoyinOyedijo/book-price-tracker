import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
genres = []

genretitles = soup.find_all('ul')[2]

for genre in genretitles.find_all('a'):
  genres.append({'name': genre.get_text(strip=True),
                 'url': 'https://books.toscrape.com/catalogue/category/' + genre['href'].replace('../', '')})

allbooks = []

for websites in genres:
  base_url = websites['url']
  name = websites['name']
  page = 1

  while True:
    if page == 1:
      url = base_url
    else:
      url = base_url.replace('index.html', f'page-{page}.html')

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('li', 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

    if not articles:
      break

    for article in articles:
      title = article.find('h3')
      rating = article.find('p', class_='star-rating')['class'][1]
      prices = article.find_all('p')[1]
      availability = False
      if article.find('p','instock availability').get_text(strip=True) == 'In stock':
        availability = True

      allbooks.append({'title': title.get_text(), 'rating': rating, 'price': float(prices.get_text().strip().replace('£', '')), 'In stock': availability, 'genre':name })

    page += 1
print(allbooks)
