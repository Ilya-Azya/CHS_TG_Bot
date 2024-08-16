from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import chs_child

router = Router()


@router.message(Text(text="Online"))
async def back_start(message: Message):
    msg = "Не нашли ответ на свой вопрос?\nОбратитесь к администратору:\n<i><a href='https://t.me/jaffast2'>Азявчиков Илья Вадимович</a></i>"
    await message.reply(
        msg, parse_mode="HTML", reply_markup=chs_child()
    )
    await message.answer(
        "Могу помочь чем-то еще?",
        reply_markup=chs_child()
    )


@router.message(Text(text="Homeshcool"))
async def back_start(message: Message):
    msg = "Не нашли ответ на свой вопрос?\nОбратитесь к администратору:\n<i><a href='https://t.me/mmalses'>Азявчикова Мария Владимировна</a></i>"
    await message.reply(
        msg, parse_mode="HTML", reply_markup=chs_child()
    )
    await message.answer(
        "Могу помочь чем-то еще?",
        reply_markup=chs_child()
    )
