from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import get_yes_no_kb, chs_child, format_learn, bills, coast_online

router = Router()


@router.callback_query(Text(text="coast_online"))
async def send_online_choise(callback: types.CallbackQuery):
    msg = "Выберите ступень обучения"
    await callback.message.answer(msg, parse_mode="Markdown", reply_markup=coast_online())
    await callback.answer()


@router.callback_query(Text(text="coast_IP"))
async def send_IP_coast(callback: types.CallbackQuery):
    msg = "Стоимость обучения в месяц — *60€*"
    await callback.message.answer(msg, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(Text(text="coast_elementary"))
async def send_IP_coast(callback: types.CallbackQuery):
    msg = "Стоимость обучения в месяц — *200€*"
    await callback.message.answer(msg, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(Text(text="coast_middle"))
async def send_IP_coast(callback: types.CallbackQuery):
    msg = "Стоимость обучения в месяц — *250€*"
    await callback.message.answer(msg, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(Text(text="coast_high"))
async def send_IP_coast(callback: types.CallbackQuery):
    msg = "Стоимость обучения в месяц —  *300€*"
    await callback.message.answer(msg, parse_mode="Markdown")
    await callback.answer()