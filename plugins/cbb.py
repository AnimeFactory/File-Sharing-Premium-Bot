# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>├⋗🧑‍💻 Creater :</b> <a href='https://t.me/Jack_AFO'>Jack</a> \n<b>├⋗📝 Language :</b> <a href='https://python.org'>Python 3</a> \n<b>├⋗📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n<b>├⋗🚀 Server :</b> <a href='https://koyeb.com'>Koyeb</a> \n<b>├⋗📢 Channel :</b> <a href='https://t.me/Anime_Carnival_4U'>Anime Carnival</a> \n<b>├⋗🧑‍💻 Developer :</b> <a href='https://t.me/Jack_AFO'>Jack</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
