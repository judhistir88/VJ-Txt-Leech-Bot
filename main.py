# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.errors.exceptions.bad_request_400 import MessageIdInvalid

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

user_data = {}  # Dictionary to hold user-specific data

@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>Hello {m.from_user.mention} 👋\n\nI Am A Bot For Download Links From Your **.TXT** File And Then Upload That File On Telegram.\n\nFor Thumb URL use direct thumb link from https://graph.org or any direct download link website\n\nDirect Download Site Example ➡️ https://postimages.org/\n\nUse /stop to stop any ongoing task.</b>")

@bot.on_message(filters.command(["stop"]))
async def restart_handler(_, m):
    await m.reply_text("**Stopped** ✅", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["upload"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('Send me the "Text File 📑" ⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("**Invalid file 📑 input.**")
        os.remove(x)
        return

    await editable.edit(f"**Total Links Found 🔗🔗** **{len(links)}**\n\n**Send from where you want to download Initial is** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    # Prompt the user to send their batch name, with the option to skip
    await editable.edit("**Now Please Send Me Your Batch Name\nIf you don't want to add, send `Skip` or any symbol/emoji of your choice**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text.strip()
    if raw_text0.lower() in ["skip"]:
        raw_text0 = ""  # Set it as an empty string if they chose to skip
    await input1.delete(True)

    # Inline buttons for resolution selection
    await editable.edit("**Send Resolution 📸**\n\nPlease choose quality:", reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton("144p", callback_data="144")],
        [InlineKeyboardButton("240p", callback_data="240")],
        [InlineKeyboardButton("360p", callback_data="360")],
        [InlineKeyboardButton("480p", callback_data="480")],
        [InlineKeyboardButton("720p", callback_data="720")],
        [InlineKeyboardButton("1080p", callback_data="1080")]
    ]))

    @bot.on_callback_query()
    async def resolution_callback(client, callback_query):
        raw_text2 = callback_query.data  # Set the resolution from callback data
        user_data[m.chat.id] = {'resolution': raw_text2}  # Store resolution data in user_data dict

        await callback_query.answer()
        try:
            if raw_text2 == "144":
                res = "256x144"
            elif raw_text2 == "240":
                res = "426x240"
            elif raw_text2 == "360":
                res = "640x360"
            elif raw_text2 == "480":
                res = "854x480"
            elif raw_text2 == "720":
                res = "1280x720"
            elif raw_text2 == "1080":
                res = "1920x1080"
            else:
                res = "UN"
        except Exception:
            res = "UN"

        try:
            # Try to edit the message safely, ensure it exists
            await callback_query.message.edit(f"Resolution set to: {res}")
            # Proceed to next step after resolution is set
            await proceed_to_caption(callback_query.message.chat.id)

        except MessageIdInvalid:
            # If message editing fails (e.g., due to message deletion), send a new message
            await callback_query.message.reply(f"Resolution set to: {res}")
            await proceed_to_caption(callback_query.message.chat.id)

# Function to ask for caption after resolution is set
async def proceed_to_caption(chat_id):
    editable = await bot.send_message(chat_id, "**Now Enter A Caption to add caption on your uploaded file\nIf you don't want to add a caption, send `Skip` or any symbol/emoji of your choice**")
    input3: Message = await bot.listen(chat_id)
    raw_text3 = input3.text.strip()  # Get the user's input
    if raw_text3.lower() in ["skip"]:
        raw_text3 = ""  # Set it as an empty string if they chose to skip

    highlighter = f"️ ⁪⁬⁮⁮⁮"  # Define the highlighter and use the caption if provided
    if raw_text3 == 'Robin':
        MR = highlighter
    else:
        MR = raw_text3
    await input3.delete(True)

    await proceed_to_thumbnail(chat_id)

# Function to ask for thumbnail after caption
async def proceed_to_thumbnail(chat_id):
    editable = await bot.send_message(chat_id, "Now send the direct download Thumb url\nTo know about Thumb url hit /start\n Or if you don't want thumbnail 🖼️ Send = `No`")
    input6 = message = await bot.listen(chat_id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "No"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
    for i in range(count - 1, len(links)):
        V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")  # .replace("mpd","m3u8")
        url = "https://" + V

        if "visionias" in url:
            async with ClientSession() as session:
                async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                    text = await resp.text()
                    url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

        elif 'videos.classplusapp' in url:
            url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'YOUR_TOKEN'}).json()['url']

        elif '/master.mpd' in url:
            id = url.split("/")[-2]
            url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

        name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
        name = f'{str(count).zfill(3)}) {name1[:60]}'

        if "youtu" in url:
            ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
        else:
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

        if "jw-prod" in url:
            cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
        else:
            cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

        # Try block continues here for downloading and processing
        try:
            cc = f'**Vid No:** {str(count).zfill(3)}.** {name1}{MR}.mkv\n**Batch** ➡️ **{raw_text0}**'
            cc1 = f'**Pdf No:** {str(count).zfill(3)}. {name1}{MR}.pdf \n**Batch** ➡️ **{raw_text0}**'
            if "drive" in url:
                try:
                    ka = await helper.download(url, name)
                    copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                    count += 1
                    os.remove(ka)
                    time.sleep(1)
                except FloodWait as e:
                    await m.reply_text(str(e))
                    time.sleep(e.x)
                    continue

            elif ".pdf" in url:
                try:
                    cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                    download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                    os.system(download_cmd)
                    copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                    count += 1
                    os.remove(f'{name}.pdf')
                except FloodWait as e:
                    await m.reply_text(str(e))
                    time.sleep(e.x)
                    continue
            else:
                Show = f"**⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️... **\n\n**📝Name:** `{name}\nQuality: {raw_text2}`\n\n**🔗URL :** `{url}`"
                prog = await m.reply_text(Show)
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await prog.delete(True)
                await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                count += 1
                time.sleep(1)
        except Exception as e:
            await m.reply_text(str(e))
            continue
except Exception as e:
    await m.reply_text(str(e))
