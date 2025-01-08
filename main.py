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


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    await m.reply_text(f"<b>Hello {m.from_user.mention} 👋\n\nI Am A Bot For Download Links From Your **.TXT** File And Then Upload That File On Telegram.\n\nSo Basically If You Want To Use Me First Send Me /upload Command And Then Follow Few Steps..\n\nFor Thumb Url use direct thumb link from https://graph.org or any direct download link website\n\nDirect Download Site Example ➡️ https://postimages.org/\n\nUse /stop to stop any ongoing task.</b>")


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped** ✅", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


# Declare a dictionary to store user data, including resolution
user_data = {}

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

        await callback_query.message.edit(f"Resolution set to: {res}")
        
    # Now that the resolution is stored, you can continue with the batch name and caption part
    # Prompt the user to enter a caption (optional)
    await editable.edit("Now Enter A Caption to add caption on your uploaded file\nIf you don't want to add a caption, send `Skip` or any symbol/emoji of your choice")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text.strip()  # Get the user's input
    if raw_text3.lower() in ["skip"]:
        raw_text3 = ""  # Set it as an empty string if they chose to skip

    highlighter = f"️ ⁪⁬⁮⁮⁮"  # Define the highlighter and use the caption if provided
    if raw_text3 == 'Robin':
        MR = highlighter
    else:
        MR = raw_text3
    await input3.delete(True)

    # Send the thumbnail URL request to the user
    await editable.edit("Now send the direct download Thumb url\nTo know about Thumb url hit /start\n Or if you don't want thumbnail 🖼️ Send = No")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "No"
    
    # Use the stored resolution in the user_data dictionary
    user_resolution = user_data.get(m.chat.id, {}).get('resolution', 'UN')

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            url = "https://" + V

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={user_resolution}][ext=mp4]/bv[height<={user_resolution}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={user_resolution}]/bv[height<={user_resolution}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            # Downloading and sending file logic...

        await m.reply_text("**All Set ✅**")
    except Exception as e:
        await m.reply_text(f"**Downloading ⬇️ Interrupted 😶**\n\n{str(e)} \n\n**Name** ➡️ {name}\n\n**Link** ➡️ `{url}`")

bot.run()
