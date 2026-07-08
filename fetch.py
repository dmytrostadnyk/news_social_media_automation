import os
import requests


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
