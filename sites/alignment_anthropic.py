"""
Adapter for alignment.anthropic.com.
 
This is the same scraping logic from the original generate_feed.py,
just reshaped to match the adapter contract: expose SOURCE_URL,
FEED_TITLE, OUTPUT_FILE, and a fetch_articles() function that returns
a list of {"title", "url", "date"} dicts.
"""

"""

"""

import datetime

import requests
from bs4 import BeautifulSoup

SOURCE_URL = "https://alignment.anthropic.com/"
FEED_TITLE = "Alignment Science Blog (unofficial feed)"
OUTPUT_FILE = "alignment-anthropic.xml"

MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",  
]

def parse_month_year(text):
    parts = text.split()
    if len(parts) == 2 and parts[0] in MONTH_NAMES and parts[1].isdigit():
        month = MONTH_NAMES.index(parts[0]) + 1
        year = int(parts[1])
        return datetime.datetime(year, month, 1, tzinfo = datetime.timezone.utc)
    return None

def fetch_articles():
    resp = requests.get(
        SOURCE_URL,
        timeout = 30,
        headers = {"User-Agent": "Mozilla/5.0 (compatible; PersonalFeedBot/1.0)"},
    )
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    articles = []
    current_date = None
    seen_urls = set()

    table_of_content = soup.select_one("div.toc")
    for child in table_of_content.children:
        if child.name == "div" and "date" in child.get("class", []):
            maybe_date = child.get_text(strip=True)
            print(maybe_date)
            current_date = parse_month_year(maybe_date)
            print(current_date)

        elif child.name == "a":
            href = child.get("href", "")
            url = href if href.startswith("http") else f"{SOURCE_URL}{href}"
            title = child.find("h3").get_text(" ", strip=True)
            desc = child.find("div", class_="description")
            description = desc.get_text(" ", strip=True) if desc else ""

            # Only add article if unique url
            if url not in seen_urls:
                seen_urls.add(url)
                articles.append(
                    {
                        "title": title[:250],
                        "url": url,
                        "date": current_date or datetime.datetime.now(datetime.timezone.utc),
                        "description": description,
                    }
                )

    return articles
