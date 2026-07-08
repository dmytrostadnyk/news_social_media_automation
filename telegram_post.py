import os
import requests


# Posting a message to a Telegram channel using the Telegram Bot API
def post_text(text: str) -> None:
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    channel_id = os.environ["TELEGRAM_CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    response = requests.post(url, data={"chat_id": channel_id, "text": text})
    response.raise_for_status()


def post_image(photo_url: str, caption: str) -> None:
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    channel_id = os.environ["TELEGRAM_CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    response = requests.post(
        url, data={"chat_id": channel_id, "photo": photo_url, "caption": caption}
    )
    response.raise_for_status()
