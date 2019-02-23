#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("/usr/local/python3.6/lib/python3.6/site-packages")
sys.path.append("/usr/local/lib/python3.5/dist-packages")
import telebot
import time
import re
import json
from telebot import types


with open('./config.json', 'r+') as config_file:
    config = json.load(config_file)
    print('Config file load successfully:\n' + str(config))
    bot_token = config['bot_token']

bot = telebot.TeleBot(bot_token)

try:
	@bot.message_handler(func=lambda message: True)
	def movement(message):
		if message.text[0] == "/" and message.reply_to_message != None and message.reply_to_message.from_user.username != "dongzuo_bot" and message.reply_to_message.from_user.username != message.from_user.username:
			pattern = re.compile('^[a-z]+$')
			if pattern.search(message.text[1::]) == None:
				send_name = str(message.from_user.first_name)
				reply_name = str(message.reply_to_message.from_user.first_name)
				bot.reply_to(message, send_name + " " + message.text[1::] + " 了 " + reply_name + " ！")

	bot.polling(none_stop=True)
except KeyboardInterrupt:
    quit()
except Exception as e:
    print(str(e))