#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys, time

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4

StartTime = time.time()

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengekspor tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Eror : Pastikan bot anda adalah Admin di Channel FOrce subs, \nperiksa kembali. ID Channel Subs kamu pada channel ke 4 ({FORCE_SUB_CHANNEL} )")
                self.LOGGER(__name__).info("Bot Stopped")
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengekspor tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Eror : Pastikan bot anda adalah Admin di Channel FOrce subs, \nperiksa kembali. ID Channel Subs kamu pada channel ke 4 ( {FORCE_SUB_CHANNEL2} )")
                self.LOGGER(__name__).info("Bot Stopped")
                sys.exit()
        if FORCE_SUB_CHANNEL3:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengekspor tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Eror : Pastikan bot anda adalah Admin di Channel FOrce subs, \nperiksa kembali. ID Channel Subs kamu pada channel ke 4 ({FORCE_SUB_CHANNEL3} )")
                self.LOGGER(__name__).info("Bot Stopped")
                sys.exit()
        if FORCE_SUB_CHANNEL4:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL4)
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengekspor tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Eror : Pastikan bot anda adalah Admin di Channel FOrce subs, \nperiksa kembali. ID Channel Subs kamu pada channel ke 4 ( {FORCE_SUB_CHANNEL4} )")
                self.LOGGER(__name__).info("Bot Stopped")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "test kirim pesan.")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Eror : Pastikan bot anda adalah Admin di Channel Database, \nperiksa kembali. ID Channel database kamu {CHANNEL_ID}")
            self.LOGGER(__name__).info("Bot Stopped")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info("Bot Telah Aktif\n\nJangan Lupa Mainkan bot t.me/chatjomblohalu_bot")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Berhenti")
