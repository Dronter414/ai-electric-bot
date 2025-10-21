import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

import os
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("⚡ Привет! Я AI-Электрик. Пришли план или опиши объект — я помогу рассчитать материалы и стоимость.")

@dp.message()
async def handle_text(message: types.Message):
    if message.photo or message.document:
        await message.answer("📄 Принял чертёж! Сейчас распознаю и рассчитаю материалы (демо-режим).")
    else:
        await message.answer(f"Ты написал: {message.text}\n\n(Скоро я превращу это в расчёт электрики ⚙️)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
