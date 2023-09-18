# Python
from aiogram import (
    Dispatcher,
    types
)
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

