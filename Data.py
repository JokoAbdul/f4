# (©) Telegram @Biawak_Store
# t.me/Biawak_Store

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """Jika Ingin Membeli VIP Kami Cek Channel @VIIPBokepMurah"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram Untuk Menyimpan File Yang Dapat Diakses Melalui Link Khusus.

 • Creator: @{}

👨‍💻 Develoved by <a href='https://t.me/Biawak_Store'>@Biawak_Store</a></b>
"""
