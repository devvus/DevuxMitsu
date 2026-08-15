import asyncio

# ✅ Fix for event loop issue
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


# --- Original bot imports ---
from MusicSp.core.bot import DevSp
from MusicSp.core.dir import dirr
from MusicSp.core.git import git
from MusicSp.core.userbot import Userbot
from MusicSp.misc import dbb, heroku

from MusicSp.logging import LOGGER


# --- Initialization calls ---
dirr()
git()
dbb()
heroku()


# --- Create bot & userbot instances ---
app = DevSp()
userbot = Userbot()


# --- Platform imports ---
from MusicSp.platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
