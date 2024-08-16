import time
import logging
import asyncio
import configparser
import pip
pip.main(['install','https://github.com/aiogram/aiogram/archive/refs/heads/dev-3.x.zip'])

from background import keep_alive

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import startquestion, chs_child_questions, payment_questions, another_questions, bills_sendler, \
    type_coast_sendler, psyh_questions, learning_questions, extra_classes_questions, not_chs_child, \
    telegram_canals_qustions, dif_questions, send_request

config = configparser.ConfigParser()
config.read("./config.ini", encoding='utf-8-sig')

TOKEN = config.get('CHS_Bot', 'bot_token')
CHANEL_PAY_ID = config.get("CHS_Bot","payment_id")
CHANEL_REQ_ID = config.get("CHS_Bot","chs_id")


class UserState(StatesGroup):
    name = State()
    type_contact = State()
    number = State()
    send_question = State()


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(startquestion.router)
    dp.include_router(chs_child_questions.router)
    dp.include_router(payment_questions.router)
    dp.include_router(another_questions.router)
    dp.include_router(bills_sendler.router)
    dp.include_router(type_coast_sendler.router)
    dp.include_router(psyh_questions.router)
    dp.include_router(learning_questions.router)
    dp.include_router(extra_classes_questions.router)
    dp.include_router(not_chs_child.router)
    dp.include_router(telegram_canals_qustions.router)
    dp.include_router(send_request.router)
    dp.include_router(dif_questions.router)

    keep_alive()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, non_stop=True, interval=0)


if __name__ == "__main__":
    asyncio.run(main())
