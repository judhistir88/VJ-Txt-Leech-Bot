import os
import time
import datetime
import aiohttp
import aiofiles
import asyncio
import logging
import requests
import subprocess
from utils import progress_bar
from pyrogram import Client, filters
from pyrogram.types import Message


def duration(filename):
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return float(result.stdout)
    except Exception as e:
        logging.error(f"Failed to retrieve duration for {filename}: {e}")
        return 0.0


def exec(cmd):
    try:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.stdout.decode()
        return output
    except Exception as e:
        logging.error(f"Command execution failed: {e}")
        return ""


async def aio(url, name):
    try:
        file_path = f"{name}.pdf"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    async with aiofiles.open(file_path, mode="wb") as f:
                        await f.write(await resp.read())
        return file_path
    except Exception as e:
        logging.error(f"Failed to download file {name}: {e}")
        return None


async def download_video(url, cmd, name, retries=3):
    download_cmd = (
        f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
    )
    for attempt in range(retries):
        try:
            logging.info(f"Executing command: {download_cmd}")
            result = subprocess.run(download_cmd, shell=True)
            if result.returncode == 0:
                file_path = [ext for ext in [".mp4", ".webm", ".mkv"] if os.path.exists(f"{name}{ext}")]
                if file_path:
                    return f"{name}{file_path[0]}"
            logging.warning(f"Retrying download: Attempt {attempt + 1} of {retries}")
            await asyncio.sleep(5)
        except Exception as e:
            logging.error(f"Download attempt failed for {name}: {e}")
    logging.error(f"Download failed after {retries} attempts for {name}")
    return None


async def send_doc(bot: Client, m: Message, cc, file_path, prog, count, name):
    try:
        reply = await m.reply_text(f"Uploading {name}...")
        start_time = time.time()
        await bot.send_document(m.chat.id, file_path, caption=cc, progress=progress_bar, progress_args=(reply, start_time))
        await reply.delete()
        os.remove(file_path)
    except Exception as e:
        logging.error(f"Failed to upload document {name}: {e}")


async def send_vid(bot: Client, m: Message, cc, filename, thumb, name, prog):
    try:
        thumb_path = f"{filename}.jpg"
        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:00:12 -vframes 1 "{thumb_path}"', shell=True)

        reply = await m.reply_text(f"Uploading video {name}...")
        dur = int(duration(filename))
        start_time = time.time()

        try:
            await bot.send_video(
                m.chat.id,
                filename,
                caption=cc,
                supports_streaming=True,
                thumb=thumb_path if thumb == "No" else thumb,
                duration=dur,
                height=720,
                width=1280,
                progress=progress_bar,
                progress_args=(reply, start_time),
            )
        except Exception:
            await bot.send_document(m.chat.id, filename, caption=cc, progress=progress_bar, progress_args=(reply, start_time))

        os.remove(filename)
        if os.path.exists(thumb_path):
            os.remove(thumb_path)
        await reply.delete()
    except Exception as e:
        logging.error(f"Failed to upload video {name}: {e}")
