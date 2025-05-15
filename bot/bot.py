import asyncio
from os import getenv, name
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot_menu import set_bot_menu
from commands import router as commands_router
from handlears import router as handlears_router
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(commands_router)
dp.include_router(handlears_router)
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await set_bot_menu(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print(f"Starting bot...")
    asyncio.run(main())