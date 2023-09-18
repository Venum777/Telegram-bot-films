# Python
import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.enums import ParseMode

# Local
from dispatcher import dp


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
