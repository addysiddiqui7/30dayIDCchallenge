#scrapping news headlines from a website

import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
    except requests.exceptions.RequestException as e:
        print("Error fetching the page:", e)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # This selector may vary depending on the site structure
    headlines = soup.find_all('h3')  # You can also try h2, h1, or specific classes

    extracted = []
    for h in headlines:
        text = h.get_text(strip=True)
        if text:
            extracted.append(text)

    return extracted

# Example usage
url = "https://www.thehindu.com/"
headlines = fetch_headlines(url)

print("\n📰 Top Headlines for today:\n")
for i, headline in enumerate(headlines[:10], 1):
    print(f"{i}. {headline}")
