import requests
from bs4 import BeautifulSoup

# Website to scrape
url = "https://quotes.toscrape.com"

# Send request to website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes
    quotes = soup.find_all("span", class_="text")

    print("Quotes from the website:\n")

    for i, quote in enumerate(quotes[:5], start=1):
        print(f"{i}. {quote.text}")

else:
    print("Failed to retrieve the webpage.")