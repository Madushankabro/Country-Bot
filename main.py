# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Country-Info-Bot/blob/main/LICENSE

import os
import pyrogram
import asyncio
import time
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Country Info Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
Hai {},

`Iam a simple country Info bot. Give me a country name I will send the informations of the country.`

👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz)
"""
HELP_TEXT = """
➠ `Just Send Me a Country Name`

➠ `I Will Send Informations`

👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz)
"""
ABOUT_TEXT = """
➠ **Bot** : Country Info Bot

➠ **Creator** : [ᴍʜᴅ ᴍᴜꜰᴀz](https://telegram.me/Mufaz123)

➠ **Channel** : @BX_Botz

➠ **Source** : [Click here](https://t.me/nokiyirunnoippokitum)

➠ **Language** : [Python3](https://python.org/)

➠ **Library** : [Pyrogram v1.2.0](https://pyrogram.org/)

➠ **Server** : [Heroku](https://heroku.com/)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/BX_Botz'),
        InlineKeyboardButton('👥Support Group', url='https://telegram.me/BxSupport')
        ],[
        InlineKeyboardButton('⚙️Help', callback_data='help'),
        InlineKeyboardButton('🔰About', callback_data='about')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data='home'),
        InlineKeyboardButton('🔰About', callback_data='about'),
        InlineKeyboardButton('🔐Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data='home'),
        InlineKeyboardButton('⚙️Help', callback_data='help'),
        InlineKeyboardButton('🔐Close', callback_data='close')
        ]]
    )
ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔰Help', callback_data='help'),
        InlineKeyboardButton('🔐Close', callback_data='close')
        ]]
    )

@FayasNoushad.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(filters.private & filters.text)
async def countryinfo(bot, update):
    country = CountryInfo(update.text)
    info = f"""
Name : `{country.name()}`
Native Name : `{country.native_name()}`
Capital : `{country.capital()}`
Population : `{country.population()}`
Region : `{country.region()}`
Sub Region : `{country.subregion()}`
Top Level Domains : `{country.tld()}`
Calling Codes : `{country.calling_codes()}`
Currencies : `{country.currencies()}`
Residence : `{country.demonym()}`
Timezone : `{country.timezones()}`
"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url=f'https://t.me/BX_Botz'),
        InlineKeyboardButton('👥Support Group', url=f'https://t.me/BX_Botz')
        ],[
        InlineKeyboardButton('💡Bot List', url='https://t.me/BX_Botz/31'),
        InlineKeyboardButton('Google', url='https://www.google.com/search?q=india')

        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except Exception as error:
        print(error)

FayasNoushad.run()
