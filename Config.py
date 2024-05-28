import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("25512251"))
    API_HASH = os.environ.get("86cf5ff56e56c4f20a7b1295b130e720")
    BOT_TOKEN = os.environ.get("6918123071:AAGgqOLJuM4kLbkBH7bMjq3ycJK9PJl2sQE")
    BOT_USERNAME = os.environ.get("sessiztagger_bot")
    BOT_NAME = os.environ.get("Sessiz Tagger")
    BOT_ID = int(os.environ.get("5125459394"))
    SUDO_USERS = os.environ.get("5710250764").split()
    SUPPORT_CHAT = os.environ.get("olimposchat")
    OWNER_ID = int(os.environ.get("5710250764"))
    OWNER_USERNAME = os.environ.get("SakirBey")
