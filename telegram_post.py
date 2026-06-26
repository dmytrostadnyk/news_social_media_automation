import os
import requests


# Posting a message to a Telegram channel using the Telegram Bot API
def post_to_telegram(text: str) -> None:
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    channel_id = os.environ["TELEGRAM_CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    response = requests.post(url, data={"chat_id": channel_id, "text": text})
    response.raise_for_status()
