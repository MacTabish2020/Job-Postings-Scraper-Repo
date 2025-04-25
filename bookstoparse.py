from bs4 import BeautifulSoup
import pandas as pd

book_data = []
serial = 1

for page_num in range(1, 51):
    with open(f'/Users/tabishbaig/Documents/Scraping Projects/BooksScraper/books_page_{page_num}.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find('h3').find('a').get('title')
        print(title)

        rating_tag = book.find('p', class_='star-rating')
        rating = ' '.join(rating_tag.get('class')) if rating_tag else 'No rating'
        print(rating)

        price_color = book.find('p', class_="price_color")
        price = price_color.text
        print(price)

        instock_availability = book.find('p', class_='instock availability')
        instock = instock_availability.text.strip()
        print(instock)

        book_data.append({
            'Serial': serial,
            'Title': title,
            'Rating': rating,
            'Price': price,
            'Availability': instock
        })
        serial += 1

df = pd.DataFrame(book_data)
df.to_csv('books_output.csv', index=False)
