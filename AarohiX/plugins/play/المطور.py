from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["المطور", "الحاكم", "كارف"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/610599a976ae27316bfd4.jpg",
        caption="• Dev Bot ↦ ميوزك الحاكم كارف \n ━━━━━━━━━━━━ \n • Dev ↦ Cr SoUrce:karef . \n • Bio ↦- 𓏺 Whoever humbles #himself to god will be #exalted 𓏺",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطورالسورس", url=f"https://t.me/KA_5N"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/SW_MS"
                    ),
                ],
            ]
        ),
    )
