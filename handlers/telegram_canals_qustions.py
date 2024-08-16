from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import tel_canal_grades, grades_online_tel_canals, grades_ip_tel_canals

router = Router()

@router.callback_query(Text(text="tel_grades"))
async def go_to_take_canal(callback: types.CallbackQuery):
    await callback.message.reply(
        "Выберите форму обучения",
        reply_markup=tel_canal_grades()
    )
    await callback.answer()


@router.callback_query(Text(text="tel_canals_online"))
async def canal_grade_online(callback: types.CallbackQuery):
    await callback.message.reply(
        "Ссылку на telegram-канал вашего класса вы моете получить у администратора",
        reply_markup=grades_online_tel_canals()
    )
    await callback.answer()


@router.callback_query(Text(text="tel_canals_IP"))
async def canal_grade_IP(callback: types.CallbackQuery):
    await callback.message.reply(
        "Ссылку на telegram-канал вашего класса вы моете получить у администратора",
        reply_markup=grades_ip_tel_canals()
    )
    await callback.answer()