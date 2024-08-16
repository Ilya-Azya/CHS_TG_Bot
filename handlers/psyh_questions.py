import logging

from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import psyh_menu, chs_child

router = Router()


@router.message(Text(text="Информация"))
async def back_start(message: Message):
    await message.reply(
        "Общая информация от Юли",
        reply_markup=psyh_menu()
    )


@router.callback_query(Text(text="contact_psyh"))
async def send_psyh_contact(callback: types.CallbackQuery):
    msg = "<b>Наш психолог:</b>\n<b>Герин Юлия Анатольевна</b>\n@julia_heryn"
    await callback.message.answer(msg, parse_mode="HTML")
    await callback.answer()


@router.callback_query(Text(text="back_main_chs"))
async def go_back_main(callback: types.CallbackQuery):
    msg = "Ну и ладно("
    await callback.message.answer(msg, parse_mode="Markdown", reply_markup=chs_child())
    await callback.answer()


@router.message(Text(text="Связаться с психологом"))
async def contact_psyh(message: Message):
    await message.reply(
        "<b>Наш психолог:</b>\n<i>Герин Юлия Анатольевна</i>\n@julia_heryn",
        parse_mode="HTML"
    )

@router.message(Text(text="Канал психолога"))
async def canal_psyh(message: Message):
    await message.reply(
        "<b>Наш психолог создал канал для общения:</b>\nссылка",
        parse_mode="HTML"
    )
