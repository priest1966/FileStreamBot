from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>Hey, </b>{}\n 
<b>I'm Telegram Files Streaming Bot As Well Direct Links Generator</b>\n
<b>Just Forward Me Any File.</b>\n
"""

    HELP_TEXT = """
<b>- sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴍᴇᴅɪᴀ</b>
<b>- ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ</b>\n
<b>🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.</b>\n
<i><b> ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ <a href='https://t.me/icecube9680_bot'>Owner</a></b></i>"""

    ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : {}</b>\n
<b>✦ ᴠᴇʀsɪᴏɴ : {}</b>
<b>✦ ᴜᴘᴅᴀᴛᴇᴅ ᴏɴ : 06-January-2024</b>
<b>✦ Owner : <a href='https://t.me/icecube9680_bot'>IceCube</a></b>\n
"""

    STREAM_TEXT = """
<i><u>Your Link Generated !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🖥 Wᴀᴛᴄʜ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>Your Link Generated !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""


    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Contact Owner](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
