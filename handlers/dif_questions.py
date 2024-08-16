import logging
from aiogram import F

from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import start_main, send_report, for_dif

router = Router()


@router.callback_query(Text(text="/help", ignore_case=True))
async def back_start(callback: types.CallbackQuery):
    await callback.message.answer(
        text="Помощь на месте!",
        reply_markup=ReplyKeyboardRemove
    )
    await callback.message.answer(
        "Для начала работы напишите _/start_\n" \
        "Или нажмите на _кнопку_ ниже\n\n" \
        "Вы так же можете ввести *рарезервированные* слова такие как\n"
        "_Оплата, Учебный процесс, Дополнительные занятия, Наши telegram-каналы\n" \
        "Частые вопросы, Мы в интернете, Порядок зачисления, Контакты, Оставить заявку_\n\n" \
        "Если вы нашли ошибку в работе бота или какие-либо недоработки - используйте команду _/bugreport_",
        parse_mode="Markdown",
        reply_markup=start_main()
    )
    await callback.answer()



@router.message(Text(text="/help", ignore_case=True))
async def back_start(message: Message):
    await message.answer(
        text="Помощь на месте!",
        reply_markup=ReplyKeyboardRemove
    )
    await message.answer(
        "Для начала работы напишите _/start_\n" \
        "Или нажмите на _кнопку_ ниже\n\n" \
        "Вы так же можете ввести *рарезервированные* слова такие как\n"
        "_Оплата, Учебный процесс, Дополнительные занятия, Наши telegram-каналы\n" \
        "Частые вопросы, Мы в интернете, Порядок зачисления, Контакты, Оставить заявку_\n\n" \
        "Если вы нашли ошибку в работе бота или какие-либо недоработки - используйте команду _/bugreport_",
        parse_mode="Markdown",
        reply_markup=start_main()
    )


@router.message(Text(text="/bugreport", ignore_case=True))
async def bug_reporting(message: Message):
    await message.reply(
        text="Если вы нашли *баги* и/или *недоработки* бота - напишите _мне_",
        parse_mode="Markdown",
        reply_markup=send_report()
    )
    await message.answer(
        "*Спасибо за помощь!*",
        parse_mode="Markdown",
    )


@router.message()
async def photo_sent(message: Message, state: FSMContext):
    if message.photo:
        await message.reply(
            "Вы прислали фото, я не знаю, что с ним делать\n"\
            "Для работы воспользуйтесь командой _/help_ или _/start_",
            parse_mode="Markdown",
            reply_markup=for_dif()
        )
    elif message.audio:
        await message.reply(
            "Вы прислали аудиофайл, я не знаю, что с ним делать\n" \
            "Для работы воспользуйтесь командой _/help_ или _/start_",
            parse_mode="Markdown",
            reply_markup=for_dif()
        )
    elif message.animation:
        await message.reply(
            "Вы прислали GIF-файл, я не знаю, что с ним делать\n" \
            "Для работы воспользуйтесь командой _/help_ или _/start_",
            parse_mode="Markdown",
            reply_markup=for_dif()
        )
    elif message.text:
        await message.reply(
            "Вы прислали непонятный для меня текст, я не знаю, что с ним делать\n" \
            "Для работы воспользуйтесь командой _/help_ или _/start_",
            parse_mode="Markdown",
            reply_markup=for_dif()
        )
    elif message.document:
        await message.reply(
            "Я вас не понимаю\n" \
            "Для работы воспользуйтесь командой _/help_ или _/start_",
            parse_mode="Markdown",
            reply_markup=for_dif()
        )
    else:
        await message.reply(
            "Для работы воспользуйтесь командой _/help_ или _/start_",
            reply_markup=for_dif()
        )