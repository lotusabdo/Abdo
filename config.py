import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","II_U_6")
USER_OWNER = getenv("USER_OWNER","II_U_6")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , None)
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , None)
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , None)
EVALOP = list(map(int, getenv("EVALOP", "6456857472").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999999990"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))



# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6456857472))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/lotusabdo/Abdo3.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")
OWNER_CHANNEL = getenv("OWNER_CHANNEL", "https://t.me/l2_2Y")
GROUP_BOT = int(getenv("GROUP_BOT", "-1002107910251"))
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION", None)
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
    "START_IMG_URL", "https://telegra.ph/file/af5a7f8f211725f3f4274.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/5eb96c4141db368f17b84.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"

##########################

BAND = [1602355282,5381851107]

########
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

if OWNER_CHANNEL:
    if not re.match("(?:http|https)://", OWNER_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","")
USER_OWNER = getenv("USER_OWNER","")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , None)
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , None)
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , None)
EVALOP = list(map(int, getenv("EVALOP", "6456857472").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999999990"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))



# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6456857432))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")
OWNER_CHANNEL = getenv("OWNER_CHANNEL", "")
GROUP_BOT = int(getenv("GROUP_BOT", "-1002107910251"))
# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION", None)
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
    "START_IMG_URL", "https://telegra.ph/file/af5a7f8f211725f3f4274.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/5eb96c4141db368f17b84.jpg"
)
PLAYLIST_IMG_URL = photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not  message.reply_photo(photo=photo, caption=
       
STATS_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
STREAM_IMG_URL = "https://graph.org/file/5eb96c4141db368f17b84.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"

photo = user.photo.big_file_id
photo = await client.download_media(photo)
if not  message.reply_photo(photo=photo, caption=
       
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/88fb55599836ef5662a98.jpg"

##########################

BAND = [1602355282,5381851107]

########
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

if OWNER_CHANNEL:
    if not re.match("(?:http|https)://", OWNER_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
