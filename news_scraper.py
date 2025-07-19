import requests
from bs4 import BeautifulSoup

# Target news website chosen: BBC
URL = "https://www.bbc.com/news"
HEADERS_FILE = "headlines.txt"

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise error if status != 200
    return response.text

def extract_headlines(html):
    soup = BeautifulSoup(html, 'html.parser')
    headlines = []

    # BBC often uses <h3> for headlines
    for tag in soup.find_all(['h2', 'h3']):
        text = tag.get_text(strip=True)
        if text and len(text) > 20:  
    # Filter out empty strings and very short titles (like 'Home' or 'Live') to keep only meaningful, full-length headlines
            headlines.append(text)

    return list(set(headlines))  # Remove duplicates

def save_to_file(headlines, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, line in enumerate(headlines, start=1):
            file.write(f"{idx}. {line}\n")

    print(f" {len(headlines)} headlines saved to {filename}")

def main():
    try:
        html = fetch_html(URL)
        headlines = extract_headlines(html)
        save_to_file(headlines, HEADERS_FILE)
    except Exception as e:
        print(" Error:", e)

if __name__ == "__main__":
    main()
