import requests

headers = {
    'User-Agent': 'Mozilla/5.0',
}

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(f'books_page_{page}.html', 'wb') as f:
            f.write(response.content)
        print(f"Downloaded page {page}")
    else:
        print(f"Failed to download page {page}, status code: {response.status_code}")
