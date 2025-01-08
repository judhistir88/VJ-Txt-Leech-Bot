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
    await m.reply_text(f"<b>Hello {m.from_user.mention} 👋\n\nI Am A Bot For Download Links From Your **.TXT** File And Then Upload That File On Telegram.\n\nFor Thumb URL use direct thumb link from https://graph.org or any direct download link website\n\nDirect Download Site Example ➔ https://postimages.org/\n\nUse /stop to stop any ongoing task.</b>")

@bot.on_message(filters.command(["stop"]))
async def restart_handler(_, m):
    await m.reply_text("**Stopped** ✅", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["upload"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('Send me the "Text File 📁" ⚡️')
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
        await m.reply_text("**Invalid file 📁 input.**")
        os.remove(x)
        return

    await editable.edit(f"**Total Links Found 🔗🔗** **{len(links)}**\n\n**Send from where you want to download. Initial is** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name\nIf you don't want to add, send `Skip` or any symbol/emoji of your choice**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text.strip()
    if raw_text0.lower() in ["skip"]:
        raw_text0 = ""
    await input1.delete(True)

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
        raw_text2 = callback_query.data
        user_data[m.chat.id] = {'resolution': raw_text2}

        await callback_query.answer()
        try:
            res = {
                "144": "256x144",
                "240": "426x240",
                "360": "640x360",
                "480": "854x480",
                "720": "1280x720",
                "1080": "1920x1080"
            }.get(raw_text2, "UN")
        except Exception:
            res = "UN"

        try:
            await callback_query.message.edit(f"Resolution set to: {res}")
            await proceed_to_caption(callback_query.message.chat.id)
        except MessageIdInvalid:
            await callback_query.message.reply(f"Resolution set to: {res}")
            await proceed_to_caption(callback_query.message.chat.id)

async def proceed_to_caption(chat_id):
    editable = await bot.send_message(chat_id, "**Now Enter A Caption to add caption on your uploaded file\nIf you don't want to add a caption, send `Skip` or any symbol/emoji of your choice**")
    input3: Message = await bot.listen(chat_id)
    raw_text3 = input3.text.strip()
    if raw_text3.lower() in ["skip"]:
        raw_text3 = ""

    highlighter = f"⁠ "
    MR = highlighter if raw_text3 == 'Robin' else raw_text3
    await input3.delete(True)

    await proceed_to_thumbnail(chat_id)

async def proceed_to_thumbnail(chat_id):
    editable = await bot.send_message(chat_id, "Now send the direct download Thumb url\nTo know about Thumb url hit /start\n Or if you don't want thumbnail 🖼️ Send = `No`")
    input6 = await bot.listen(chat_id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "No"

    count = int(raw_text) if len(links) > 1 else 1
    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            ytf = f"b[height<={user_data[m.chat.id]['resolution']}]/bv+ba"
            cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'**Vid No:** {str(count).zfill(3)}. **{name1}{MR}.mkv**\n**Batch** ➔ **{raw_text0}**'
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name, None)
                count += 1
                time.sleep(1)
            except Exception as e:
                await m.reply_text(str(e))
                continue
    except Exception as e:
        await m.reply_text(str(e))

bot.run()
