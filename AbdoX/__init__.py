from AbdoX.core.bot import Zelzaly
from AbdoX.core.dir import dirr
from AbdoX.core.userbot import Userbot
from AbdoX.misc import dbb, heroku

from .logging import LOGGER

dirr()
dbb()
heroku()

app = Zelzaly()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
