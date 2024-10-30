from aiogram import types
from data.config import ADMINS
from loader import dp




# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    text = message.text



