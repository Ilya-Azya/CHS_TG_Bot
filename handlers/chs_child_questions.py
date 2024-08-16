import logging
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.for_questions import get_yes_no_kb, payment_kb_choice, format_learn
from keyboards.for_questions import learn_proc_questions, extra_classes, psyh_questions, tel_canals

router = Router()


@router.message(Text(text="Назад"))
async def back_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Обучаетесь ли вы у нас?",
        reply_markup=get_yes_no_kb()
    )


@router.message(Text(text="Оплата"))
async def payment(message: Message):
    await message.reply(
        "Что именно вас интересует?",
        reply_markup=payment_kb_choice()
    )


@router.message(Text(text="Учебный процесс"))
async def learning(message: Message):
    await message.reply(
        "Выберите, что именно вас интересует",
        reply_markup=learn_proc_questions()
    )


@router.message(Text(text="Ничего из этого"))
async def nothing(message: Message):
    await message.reply(
        "Выберите формат обучения",
        reply_markup=format_learn()
    )


@router.message(Text(text="Психолог"))
async def psyh(message: Message):
    await message.reply(
        "Что именно вас интересует?",
        reply_markup=psyh_questions()
    )


@router.message(Text(text="Дополнительные занятия"))
async def extra(message: Message):
    await message.reply(
        "Что именно вас интересует?",
        reply_markup=extra_classes()
    )

@router.message(Text(text="Наши telegram-каналы"))
async def tel_canals_main(message: Message):
    await message.reply(
        "Какой канал вас интересует?",
        reply_markup=tel_canals()
    )