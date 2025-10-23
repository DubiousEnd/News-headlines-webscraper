# task3_webscraper.py
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        headlines = []
        for tag in soup.find_all(['h2']):
            text = tag.get_text(strip=True)
            if text:
                headlines.append(text)
        
        return headlines

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, line in enumerate(headlines, start=1):
            f.write(f"{i}. {line}\n")
    print(f" Saved {len(headlines)} headlines to {filename}")

if __name__ == "__main__":
    news_url = "https://timesofindia.indiatimes.com/gcc"
    headlines = fetch_headlines(news_url)
    save_to_file(headlines)
