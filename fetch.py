import os
import requests
import feedparser
from trafilatura import fetch_url, extract


# Fetching an image from Pexels based on a query created by an LLM using the Pexels API
def fetch_image_from_pexels(image_query: str) -> str:
    pexels_api_key = os.environ["PEXELS_API_KEY"]
    url = "https://api.pexels.com/v1/search"
    response = requests.get(
        url,
        params={"query": image_query, "per_page": 1, "orientation": "landscape"},
        headers={"Authorization": pexels_api_key},
    )
    response.raise_for_status()
    photos = response.json()["photos"]
    if not photos:
        raise ValueError(f"No images found for query: {image_query}")
    return photos[0]["src"]["large"]

# Fetching an article link from RSS feed using feedparser
def fetch_article_from_rss() -> str:
    feed = feedparser.parse("https://feeds.bbci.co.uk/news/business/rss.xml")
    entry = feed.entries[0]
    return entry.link

# Fetching an article text from a URL extracted from RSS feed
def fetch_article_text() -> str:
    article_url = fetch_url(entry.link)
    article = extract(article_url, with_metadata=False, include_comments=False)
    return article