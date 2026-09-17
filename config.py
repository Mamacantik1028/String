import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PICS = os.environ.get(
    "PICS",
    "https://ibb.co/HLN6W7Bg"
).split()

ADMIN = int(os.environ.get("ADMIN", "0"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"

AUTH_CHANNELS = list(
    map(int, os.environ.get("AUTH_CHANNELS", "").split())
)

AUTH_REQ_CHANNELS = list(
    map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())
)

FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", "2"))
