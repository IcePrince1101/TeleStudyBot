from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
import logging

# * import bot with handlers
# import handlers


API_TOKEN = 'YOUR TOKEN'

# * Initilazing bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# * Logging setup
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)

# * Handler for /start command
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я бот с вопросами для студентов Школы21! Выбери направление, в котором хочешь потренироваться.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
