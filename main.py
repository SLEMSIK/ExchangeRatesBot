import requests
import xml.etree.ElementTree as ET
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='') # Write your bot token here
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне сокращённое название валюты и я отправлю её курс к рублю (пример: USD,EUR)\n\nРазработчик SLEMSIK - https://github.com/SLEMSIK")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id,f'✅ Курс валюты {msg.text} к рублю: ' + ET.fromstring(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text).find(
	f"./Valute[CharCode='{msg.text}']/Value").text.replace(',', '.')+ f'\nИнформация получена с сайта ЦБ РФ 🇷🇺')

executor.start_polling(dp)