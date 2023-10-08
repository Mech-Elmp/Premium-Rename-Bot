"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 10GB
	Price 0
	
	**🥉 Bronze Tier 🥉** 
	Daily  Upload  limit 20GB
	Price Rs 19  ind /🌎 0.25$  per Month
	
	**💫 Silver Tier 💫**
	Daily Upload limit 50GB
	Price Rs 39  ind /🌎 0.45$  per Month
	
	**🔘 Platinum Tier 🔘**
	Daily Upload limit 100GB
	Price Rs 69  ind /🌎 0.80$  per Month

        **🪙 Gold Tier 🪙**
	Daily Upload limit 500GB
	Price Rs 99  ind /🌎 1.20$  per Month        

        **💎 Diamond 💎**
	Daily Upload limit Unlimited
	Price Rs 199  ind /🌎 2.40$  per Month       
	
	
	Pay Using Upi I'd `hp148981@paytm`
	
	After Payment Send Screenshots Of Payment To Admin @Mrkiller_1109"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Mrkiller_1109")], 
        			[InlineKeyboardButton("Paytm",url = "https://graph.org/file/31706dbeac09ceb90f8cd.jpg"),
        			InlineKeyboardButton("Google Pay",url = "https://graph.org/file/474c3568c13193a8f5811.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 10GB
	Price 0
	
	**🥉 Bronze Tier 🥉** 
	Daily  Upload  limit 20GB
	Price Rs 19  ind /🌎 0.25$  per Month
	
	**💫 Silver Tier 💫**
	Daily Upload limit 50GB
	Price Rs 39  ind /🌎 0.45$  per Month
	
	**🔘 Platinum Tier 🔘**
	Daily Upload limit 100GB
	Price Rs 69  ind /🌎 0.80$  per Month

        **🪙 Gold Tier 🪙**
	Daily Upload limit 500GB
	Price Rs 99  ind /🌎 1.20$  per Month        

        **💎 Diamond 💎**
	Daily Upload limit Unlimited
	Price Rs 199  ind /🌎 2.40$  per Month
	
	
	Pay Using Upi I'd `hp148981@paytm`
	
	After Payment Send Screenshots Of Payment To Admin @Mrkiller_1109"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Mrkiller_1109")], 
        			[InlineKeyboardButton("Paytm",url = "https://graph.org/file/31706dbeac09ceb90f8cd.jpg"),
        			InlineKeyboardButton("Phone Pay",url = "https://graph.org/file/474c3568c13193a8f5811.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
