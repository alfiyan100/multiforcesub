# File-to-link-bot

Telegram Bot untuk menyimpan Posting dan Dokumen dan dapat Diakses melalui Tautan Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.....😇.

##
### Cara install
#### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/renggi06/ForceSubMultiChannel2)</br>
<a href="https://t.me/chatjomblohalu_bot">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

#### Deploy in your VPS
````bash
git clone https://github.com/davi78/file-to-link
cd File-to-link-bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Perintah khusus admin

```
/start - Perintah start

/batch - Perintah untuk membuat lebih dari satu postingan

/genlink - Perintah untuk membuat satu postingan

/users - Perintah untuk melihat statistik bot

/broadcast - Perintah broadcast ke semua users

/uptime - melihat status bot aktif
```

### Perintah khusus user
```
/ping - cek status bot
```

### Variables 

* `API_HASH` Dapatkan API_HASH dari from my.telegram.org
* `API_ID` Dapatkan API_ID dari my.telegram.org
* `TG_BOT_TOKEN` Dapatkan Token bot dari @BotFather
* `OWNER_ID` Masukkan ID telegram OWNER
* `CHANNEL_ID` Channel ID kamu eg:- -100xxxxxxxx
* `ADMINS` ID admin
* `START_MESSAGE` Pesan start 
* `FORCE_SUB_MESSAGE` Force subs pesan 
* `FORCE_SUB_CHANNEL` Force subs 
* `FORCE_SUB_CHANNEL2` Force subs 2
* `FORCE_SUB_CHANNEL3` Force subs 3
* `FORCE_SUB_CHANNEL4` Force subs 4
* `PROTECT_CONTENT` Protect_Contect True

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

##

   **Jangan lupa bintangnya ⭐⭐⭐**
