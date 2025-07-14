#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23283708"))
API_HASH = environ.get("API_HASH", "7805011fb84729023531f0fa3f000bec")
BOT_TOKEN = environ.get("BOT_TOKEN", "7753162258:AAFKHnQEy1pk940mmDNN7b8MtZ9Oqt6TM")
OWNER = int(environ.get("OWNER", "6481888008"))
CREDIT = "𝗚𝘂𝗺𝗻𝗮𝗮𝗺"
AUTH_USER = os.environ.get('AUTH_USERS', '6481888008').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
