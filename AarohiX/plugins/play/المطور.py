from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور", "مبرمج السورس", "كارف"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/7994175c9bbea45fc7377.jpg",
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
                        "Updates", url=f"https://t.me/vzo_a"
                    ),
                ],
            ]
        ),
    )
