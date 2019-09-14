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
import random
from telebot import types


with open('./config.json', 'r+') as config_file:
    config = json.load(config_file)
    print('Config file load successfully:\n' + str(config))
    bot_token = config['bot_token']

bot = telebot.TeleBot(bot_token)
emoji = '❤️🥳😘😍☺️😉😏🙊😅😭🤣😂😅😇😤🤬😡🥵👻🙈'

try:
	last_time_forwarded_cao = 0
	last_time_repeated = 0
	last_time_greeting = 0
	@bot.message_handler(func=lambda message: True)
	def all(message):
		global last_time_forwarded_cao
		global last_time_repeated
		global last_time_greeting
		curr_time = time.time()
		randNum = random.randint(0, 100)

		if randNum % 10 == 0 and curr_time - last_time_repeated >= 600:
			last_time_repeated = time.time()
			bot.reply_to(message, message.text)
		
		if message.text == '草' and curr_time - last_time_forwarded_cao >= 300:
			last_time_forwarded_cao = time.time()
			if randNum % 2 == 0:
				bot.reply_to(message, '草')
			else:
				bot.send_sticker(message.chat.id, 'CAADBQADawADvXbGBYun-zdWQQwmFgQ')
		
		if message.text[0] == "/" and message.reply_to_message != None and message.reply_to_message.from_user.username != "littlebear_group_helper_bot" and message.reply_to_message.from_user.username != message.from_user.username and len(message.text) <= 10:
			send_name = str(message.from_user.first_name)
			reply_name = str(message.reply_to_message.from_user.first_name)
			if randNum % 3 == 0:
				text = '[{send_name}](tg://user?id={from_id}) {movement}  了 [{reply_name}](tg://user?id={reply_id}) ！{emoji}'.format(send_name=send_name, from_id=str(message.from_user.id), movement=message.text[1::], reply_name=reply_name, reply_id=str(message.reply_to_message.from_user.id), emoji=emoji[randNum % (len(emoji)-1)])
				bot.reply_to(message, text, parse_mode="Markdown")
			else:
				text = '[{send_name}](tg://user?id={from_id}) {movement}  失败了 [{reply_name}](tg://user?id={reply_id}) ！{emoji}'.format(send_name=send_name, from_id=str(message.from_user.id), movement=message.text[1::], reply_name=reply_name, reply_id=str(message.reply_to_message.from_user.id), emoji=emoji[randNum % (len(emoji)-1)])
				bot.reply_to(message, text, parse_mode="Markdown")
		
		if message.from_user.id == 704759255 and curr_time - last_time_greeting >= 300:
			last_time_greeting = time.time()
			bot.reply_to(message, '给奶奶请安！')

	bot.polling(none_stop=True)
except KeyboardInterrupt:
    quit()
except Exception as e:
    print(str(e))