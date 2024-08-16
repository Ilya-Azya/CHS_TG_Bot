from aiogram import types, Bot
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, InputMediaDocument
from keyboards.for_questions import retake_info_bill, grade_menu, book_grade_menu, retake_info, bills

router = Router()


@router.message(Text(text="Электронный журнал"))
async def el_journal(message: Message):
    await message.answer(
        "Выберите класс",
        reply_markup=grade_menu()
    )


@router.message(Text(text="Учебные пособия"))
async def books(message: Message):
    await message.answer(
        "Выберите класс",
        reply_markup=book_grade_menu()
    )


@router.message(Text(text="Пересдачи"))
async def retakes(message: Message):
    await message.answer(
        "В *Cambridge High School* существует платная система пересдач, с помощью которой вы _можете_ исправить свои отметки по необходимым предметам.\nМы надеемся, что с помощью этой функции вы _сможете_ улучшить свои результаты.\nСтоимость пересдачи — *15€*",
        parse_mode="Markdown",
        reply_markup=retake_info()
    )


@router.callback_query(Text(text="main_info_retake"))
async def send_info_retake(callback: types.CallbackQuery):
    msg = "Пересдать можно любой тип работы.\nДля того, чтобы записаться на пересдачу, необходимо:\n_1. Оплатить_ *15€*_, выбрав подходящие реквизиты\n2. Отправить квитанцию об оплате сюда или администратору\n3. Согласовать день и время пересдачи с администратором\n4. Выполнить работу и узнать результат_"
    await callback.message.answer(
        msg,
        parse_mode="Markdown",
        reply_markup=retake_info_bill(),
    )
    await callback.answer()


@router.callback_query(Text(text="retake_bills"))
async def send_bills(callback: types.CallbackQuery):
    msg = "По реквизитам какой страны вам будет удобно оплатить?"
    await callback.message.answer(msg, reply_markup=bills())


@router.message(Text(text="Правила CHS"))
async def send_doc(message: Message, bot: Bot):
    chat_id = message.from_user.id
    await bot.send_document(chat_id=chat_id,
                            document="https://chschool.eu/assets/img/08.docs/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%20CHS.pdf")
