from aiogram import Bot, Dispatcher, types
from aiogram.methods import DeleteWebhook
from aiogram.filters import Command
import asyncio
import requests
import os

from config import TXT_EXAPMLES, URL
TOKEN_API = os.environ.get("token_tg")


dp = Dispatcher()
bot = Bot(TOKEN_API)


@dp.message(Command(commands='start'))
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=TXT_EXAPMLES["start"])
    

@dp.message()
async def echo(message: types.Message):
    print(message)
    response = requests.post(url=URL, params={"question_str": message.text})
    await message.answer(f"{response.text}")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())
