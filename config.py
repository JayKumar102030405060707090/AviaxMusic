import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("29029280"))
API_HASH = getenv("68d352387daaa3abf414f4f2fa05fde6")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7206200174:AAGv0fZTNr66-c_IWc05ZlNQj2uhee3xpbw")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("-1002323533924", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("7168729089", None))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/CyberPixelPro/AviaxMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Darkworldlove")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Darkworld_Officiall")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("BQG686AAJjcaKBPjGZaXY-qw0LRXLWfMhv6qy98zttN3ahIa-nIBtOTibjAT8PTToFS9HkOltvhOb61xyuUC3u3vowQW9rFdfkzHlocLGMLPCVC4UJmI-eGMF3Nagj5g5vl_XBZb7GOeZadLhvgeAR0vilKP3bbYwX-IfOguPo-pUUZjI1pvhNbvFx7XcT_bEg7w-PtVcxyNoC3yXwwUH41bNpV5yN1mobIy_aeEGtLglACZ4SaV2MGhX38Jv0NdWcYaCHv_xhQO3dpEHnoK7bAdj--NVQ3JQWjh6SXj-zp3oG2PjbZdAkpeMzc9PzN3fta1ZunzmHzDTAQTLhQo3B2JFD5u8gAAAAHLmYa9AQ", BQG686AAJjcaKBPjGZaXY-qw0LRXLWfMhv6qy98zttN3ahIa-nIBtOTibjAT8PTToFS9HkOltvhOb61xyuUC3u3vowQW9rFdfkzHlocLGMLPCVC4UJmI-eGMF3Nagj5g5vl_XBZb7GOeZadLhvgeAR0vilKP3bbYwX-IfOguPo-pUUZjI1pvhNbvFx7XcT_bEg7w-PtVcxyNoC3yXwwUH41bNpV5yN1mobIy_aeEGtLglACZ4SaV2MGhX38Jv0NdWcYaCHv_xhQO3dpEHnoK7bAdj--NVQ3JQWjh6SXj-zp3oG2PjbZdAkpeMzc9PzN3fta1ZunzmHzDTAQTLhQo3B2JFD5u8gAAAAHLmYa9AQ)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/bd0891a681cf77b51fc74-3e4b9763f94b7f5741.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org//file/389a372e8ae039320ca6c.png"
)
PLAYLIST_IMG_URL = "https://graph.org//file/3dfcffd0c218ead96b102.png"
STATS_IMG_URL = "https://graph.org//file/99a8a9c13bb01f9ac7d98.png"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
