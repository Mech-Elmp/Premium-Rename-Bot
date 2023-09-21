import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"🤖 My Name :- <a href='https://t.me/PremiumRenameRobot'>Rename Pro⚡</a>\n❤️ Developer :- <a href='https://t.me/Mrkillet_1109'>This Person</a>\n🎀 Language :- Python3\n🎉 Library :- Pyrogram 2.0\n❤️‍🩹 Server :- Heroku\n🔘 Total Renamed File :- {total_rename}\n👀 Total Size Renamed :- {humanbytes(int(total_size))} \n\nThank you **<a href='https://t.me/Hpbot_update'>This Person</a>** for your hard work \n\n❤️ We love you <a href='https://t.me/Mrkiller_1109'>**This Person**</a> ❤️",quote=True)
