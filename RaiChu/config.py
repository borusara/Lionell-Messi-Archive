## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAQeIIaejY6HsY2l_T_PfmjpKkbBvm8WAy-2kfRYHWnpDoLQ7x_-aX_TnsSHWLV47wz9UZnL3_trUxSeNPE7A83P_T14SzcupysJhMergatU4b95JBMVNmB73TTXTfLNj3Ds45HMiy287UhDFOzcMLXOCtvPWP0r9UyXWGjEevuULGdu57iq_r54Dr5VDvwK0snhwHmz27oEQT6W2Tq6A9M2iLxsCdJDl7ZpleSWvMLAzmSaGXBhiE7qP8DvcydC-1__7p9b4aLaH0z_grK-iqriAXmALx5LOc0ksGQ0Fa59C9WeypMUtqS6r-69DaIUtFM3DQdlTn4OUBmHps2t6aCAAAAAXMtSCcA")
BOT_TOKEN = getenv("BOT_TOKEN", "6086098839:AAGn5rlcAcO1g_nkut2PjdBODpWi5j5vDqM")
BOT_NAME = getenv("BOT_NAME", "Kizuna")
API_ID = int(getenv("API_ID", "9176863"))
API_HASH = getenv("API_HASH", "afff208ad0de11acfc946ca6dcd74aec")
OWNER_NAME = getenv("OWNER_NAME", "ᴾᴿᴵᴹᴱ LOST⋆『最高』")
ALIVE_NAME = getenv("ALIVE_NAME", "Kizuna A.I")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Kizunaxassistant")
BOT_USERNAME = getenv("BOT_USERNAME","Kizunaxmusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "KizunaxAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT","https://t.me/primes_arena")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","https://t.me/PrimesDivision")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5764124248 2005266280 5217363292").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ~").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b4bbb97247397a4f4e1b2.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
