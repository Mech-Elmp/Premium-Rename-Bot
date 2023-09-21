from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("Share Your Link" ,url=f"https://t.me/share/url?url=https://t.me/PremiumRenameRobot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Refer And Earn Get 2 GB Upload Limit\nPer Refer 2 GB\n ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
