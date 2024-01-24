from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("24301715", ""))
API_HASH = getenv("cb4f7937fdd67632695f6677aef90197")

ASS_HANDLER = list(getenv("Cutie_musicx", ".").split())
BOT_TOKEN = getenv("6425591334:AAF32OS-AsyAe7nYrD7kgAjtjS4SVz3ODiM")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("6612947670"))
MONGO_DB_URI = getenv("mongodb+srv://Lakshay3434:QoFQoovNEFpV8hMf@cluster0.gqe5wwk.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("6612947670", "").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("https://telegra.ph/file/c5952790fa8235f499749.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AbishnoiMF ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/Abishnoi_bots ")

STRING_SESSION = getenv("BQFy0JMAutRVq8g9zUknwRyckrG-2dOcuyp_JQmHTnrYbGCBMivp-oGioTvTntfd1j9DGfwC6EgUTiq2p7Fy87S3dvZFbh2HAiHSQUDcrpvjw7DrZkiJXg7T9lb1LSRZuAOaaODj9em8JzJlF4SvZTuiju_CvvFaPz5lpDxSSOLtiJSX9ecm80BquaNOyXVT8OQWxd_dfwm_QqivEKYYO6zBKgLydeK5UY2Z1yvMKyIU3H2id1TZboH6Wk_XeYVTUhn8-IoxOKwbXE5ypc3r1NWgl9MmdDPMa0YAMwYPcXax2hcRrrJ_YpFgGBIZSgyHZoperiuXzt3UAY968x2g07zgIAgAAAAAGKKZLWAA", None)
SUDO_USERS = list(map(int, getenv("6612947670", "1452219013").split()))
