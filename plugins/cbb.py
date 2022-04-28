#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        text = f"<b>🥷 ᴘᴇᴍʙᴜᴀᴛ : <a href='tg://user?id={OWNER_ID}'>ᴏʀᴀɴɢ ɪɴɪ</a>\n"
        text += f"🔗 ᴄʜᴀɴɴᴇʟ 𝟷 : <a href='{client.invitelink}'>ᴅɪsɪɴɪ</a>\n"
        text += f"🔗 ᴄʜᴀɴɴᴇʟ 2 : <a href='{client.invitelink2}'>ᴅɪsɪɴɪ</a>\n"
        text += f"🔗 ᴄʜᴀɴɴᴇʟ 3 : <a href='{client.invitelink3}'>ᴅɪsɪɴɪ</a>\n"
        text += f"🔗 ᴄʜᴀɴɴᴇʟ 4 : <a href='{client.invitelink4}'>ᴅɪsɪɴɪ</a></b>"
        await query.message.edit_text(
            text,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 ᴄʜᴀᴛ ʙᴏᴛ", url='t.me/admnzidbot')
                    ],

                    [
                        InlineKeyboardButton("🤖 ᴘᴀᴘ ʙᴏᴛ", url='t.me/donasinzidbot')
                    ],

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
