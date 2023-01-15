import openai
import asyncio
import json
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN, API_KEY
from aiogram.types import Message
from aiogram import types

storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML', disable_web_page_preview=True)
dp = Dispatcher(bot, storage=storage, loop=loop)
openai.api_key = API_KEY
re="\033[1;31m"
gr="\033[1;32m"
ye="\033[1;33m"
cy="\033[1;36m"

@dp.message_handler(commands=['start'])
async def start(message):
  await bot.send_message(message.chat.id, f'Привет. Это нейросеть ChatGPT. Я сканирую весь интернет и отвечаю на освнове этих данных. Прежде чем публиковать и использовать эти данные - перепроверь')



@dp.message_handler(content_types=['text'])
async def handle_text(message):
  # Получаем текст сообщения
  text = message.text
  response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=text,
  max_tokens=1024,
  temperature=0.5,
  )
  data = json.dumps(response)
  dat = json.loads(data)
  choi = dat['choices'][0]['text']
  print(f"""Запрос от {cy}@{message.from_user.username}: 
    {ye}Запрос: {gr}{message.text} 
    {ye}Ответ ChatGPT:{gr}{choi}
    """)
  await bot.send_message(message.chat.id, choi)
  print(f"{ye}------------------------------------")
  
  # Используем GPT-3 для генерации ответ

executor.start_polling(dp)