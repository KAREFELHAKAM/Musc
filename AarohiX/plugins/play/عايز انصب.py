from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config
from pyrogram.errors import FloodWait




@app.on_message(filters.command(["عاوز انصب","عاوزه انصب"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://telegra.ph/file/5ec57dbb999310e0470d7.mp4",
        caption="◍ يمكنك الان التواصل مع المطور او قم بالانضمام في جروب الدعم  :https://t.me/KA_5N للمطورين ❲ [اطغط هنا](https://t.me/SW_MV) ❳ \n\n√",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
