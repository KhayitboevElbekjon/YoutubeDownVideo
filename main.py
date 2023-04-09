from config import *
import os
from aiogram import *
from pytube import YouTube
token='5855817176:AAHcYvLuNmZQn--Tc-rJJTffLPYDwCUvPKI'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id , "Assalomu alaykum botimiz foydalanuvchisi, bu bot Youtube dan video yuklaydi\n"
                                     "Linkni jonating bo'ling tez-tez😊")


@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == "https://youtu.be/" or "https://youtube.com/" :
        await bot.send_message(chat_id, "Biroz kuting, yuklanmoqda-aa!\n"
                                        "Yana ketib qolmang😉,ozgina kutasz holos!")
        await download_youtube_video(url, message, bot)
    else:
        await bot.send_message(chat_id, ":(")


async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_lowest_resolution().download(f"{message.chat.id}", f"{message.chat.id}_{yt.title}")
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", "rb") as video:
        await bot.send_video(message.chat.id, video, caption="*Mana sizng videoingiz!*", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")



if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)