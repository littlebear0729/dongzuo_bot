#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("/usr/local/python3.6/lib/python3.6/site-packages")
sys.path.append("/usr/local/lib/python3.5/dist-packages")
import telebot
import time
from telebot import types


bot = telebot.TeleBot("REPLACE YOUR TOKEN HERE")
action = ["摸头", "揉脸", "摸摸头", "捏脸", "啪", "抓住", "推开"]
group_id = ["-1001238300697", "-1001323381880"]



@bot.message_handler(func=lambda message: True)
def movement(message):
	print(message.chat.id)
	if str(message.chat.id) in group_id:
		if message.text[0] == "/" and message.reply_to_message != None and if message.reply_to_message.from_user.username != "dongzuo_bot":
			if message.text[1::] in action:
				send_name = str(message.from_user.first_name)
				reply_name = str(message.reply_to_message.from_user.first_name)
				bot.reply_to(message, send_name + " " + message.text[1::] + " 了 " + reply_name + " ！")




bot.polling()
