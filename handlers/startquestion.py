import emoji

import logging
from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import get_yes_no_kb,chs_child, not_for_child_chs

router = Router()

@router.callback_query(Text(text="/start"))
async def cmd_start(callback: types.CallbackQuery):
    user_id = callback.message.from_user.id
    user_name = callback.message.from_user.first_name
    user_full_name = callback.message.from_user.full_name
    logging.info(f'{user_id} || {user_full_name}')
    msg = f'*Добро пожаловать, {user_name}!*\n_Я Бот от Cambridge High School_.'
    await callback.message.reply(msg, parse_mode="Markdown")
    await callback.message.answer(
        "Являетесь ли вы учеником нашей школы?",
        reply_markup=get_yes_no_kb()
    )
    await callback.answer()





@router.message(Text(text="/start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} || {user_full_name}')
    msg = f'*Добро пожаловать, {user_name}!*\n_Я Бот от Cambridge High School_.'
    await message.reply(msg, parse_mode="Markdown")
    await message.answer(
        "Являетесь ли вы учеником нашей школы?",
        reply_markup=get_yes_no_kb()
    )


@router.message(Text(text="Да"+ emoji.emojize(":OK_hand:")))
async def answer_yes(message: Message):
    await message.reply(
        "Спасибо, что остаетесь с нами!"
    )
    await message.answer(
        "Чем я могу вам помочь?",
        reply_markup=chs_child(),
    )


@router.message(Text(text="Нет"+ emoji.emojize(":cross_mark_button:")))
async def answer_no(message: Message):
    await message.answer(
        "Чем я могу вам помочь?",
        reply_markup=not_for_child_chs()
    )
