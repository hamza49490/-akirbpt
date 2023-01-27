import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("3793309"))
    API_HASH = os.environ.get("fe42ab8e509ea3f4628e82de05f3f1e3")
    BOT_TOKEN = os.environ.get("5125459394:AAHQaPvKN66HJJlsnQIB5B-c4r-BouJzmd0")
    BOT_USERNAME = os.environ.get("KaptanTaggerBot")
    BOT_NAME = os.environ.get("Kaptan Tagger")
    BOT_ID = int(os.environ.get("5125459394"))
    SUDO_USERS = os.environ.get("1948748468").split()
    SUPPORT_CHAT = os.environ.get("KaptanSupportGroup")
    OWNER_ID = int(os.environ.get("1948748468"))
    OWNER_USERNAME = os.environ.get("SakirBey1")
