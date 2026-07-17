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
def fetch_article_link() -> str:
    feed = feedparser.parse("https://feeds.bbci.co.uk/news/business/rss.xml")
    if not feed.entries:
        raise ValueError("No entries found in the RSS feed")
    entry = feed.entries[0]
    article_url = entry.link
    return article_url


# Fetching an article text from a URL extracted from RSS feed
def fetch_article_text(article_url: str) -> str:
    article = fetch_url(article_url)
    if not article:
        raise ValueError(f"Could not fetch article from URL: {article_url}")
    article_text = extract(article, with_metadata=False, include_comments=False)
    if not article_text:
        raise ValueError(f"Could not extract article text from URL: {article_url}")
    return article_text
