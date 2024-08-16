import aiogram.exceptions
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
import emoji
import configparser
from aiogram import types, Bot
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from keyboards.for_questions import chs_child, format_learn, bills, coast_type, save_bill

router = Router()

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')

CHANEL_ID = config.get('CHS_Bot', 'payment_id')


class Send_Payment(StatesGroup):
    name = State()
    grade = State()
    type_payment = State()
    document = State()
    send_que = State()


@router.message(Text(text="Вернуться назад"))
async def back_chs_child(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Слушаюсь, " + message.from_user.full_name,
        reply_markup=chs_child()
    )


@router.message(Text(text="Узнать стоимость"))
async def back_chs_child(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Выберите формат обучения",
        reply_markup=coast_type()
    )


@router.message(Text(text="Реквизиты"))
async def back_chs_child(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "По реквизитам какой страны вам будет удобно оплатить?",
        reply_markup=bills()
    )


@router.message(Text(text="Другой вопрос"))
async def back_chs_child(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Выберите формат обучения",
        reply_markup=format_learn()
    )


@router.message(Text(text="Отправить квитанцию"))
async def save_bill_bd(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "*Для сохранения квитанции введите следующие данные:*",
        parse_mode="Markdown"
    )
    await message.answer(
        "Введите ФИО ребенка"
    )
    await state.set_state(Send_Payment.name)


@router.message(Send_Payment.name)
async def save_type_payment(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer(
        "Отлично! Введите класс и форму обучения"
    )
    await state.set_state(Send_Payment.grade)


@router.message(Send_Payment.grade)
async def save_type_payment(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    await message.answer(
        "Отлично! Введите тип платежа\n(обучение/регистрация/пересдача/факультатив)"
    )
    await state.set_state(Send_Payment.type_payment)


@router.message(Send_Payment.type_payment)
async def save_type_payment(message: Message, state: FSMContext):
    await state.update_data(type_payment=message.text)
    await message.answer(
        "Прикрепите квитанцию (фото или документ)"
    )
    await state.set_state(Send_Payment.document)


@router.message(Send_Payment.document)
async def save_type_payment(message: Message, state: FSMContext, bot: Bot):
    flag = False
    if message.photo is not None:
        await state.update_data(doc=message.photo[-1].file_id)
        flag = True
        data = await state.get_data()
        text = f"ФИО ребнка: {data['username']}\n" \
               f"Класс и форма обучения: {data['grade']}\n" \
               f"Тип платежа: {data['type_payment']}\n"
        await state.set_state(Send_Payment.send_que)
        await bot.send_photo(chat_id=message.from_user.id, photo=message.photo[-1].file_id, caption=text)
        await message.answer(
            "*Проверьте правильность данных*",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Все верно" + emoji.emojize(":OK_hand:")),
                        KeyboardButton(text="Заполнить заново" + emoji.emojize(":cross_mark_button:"))
                    ]
                ],
                resize_keyboard=True,
            ),
        )
    elif message.document is not None:
        await state.update_data(doc=message.document.file_id)
        flag = True
        data = await state.get_data()
        text = f"ФИО ребнка: {data['username']}\n" \
               f"Класс и форма обучения: {data['grade']}\n" \
               f"Тип платежа: {data['type_payment']}\n"
        await state.set_state(Send_Payment.send_que)
        await bot.send_document(chat_id=message.from_user.id, document=message.document.file_id, caption=text)
        await message.answer(
            "*Проверьте правильность данных*",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Все верно" + emoji.emojize(":OK_hand:")),
                        KeyboardButton(text="Заполнить заново" + emoji.emojize(":cross_mark_button:"))
                    ]
                ],
                resize_keyboard=True,
            ),
        )
    else:
        await message.reply("Я не понимаю, что вы прислали, попробуйте еще раз")
        await state.set_state(Send_Payment.document)


@router.message(Send_Payment.send_que, Text(text="Все верно" + emoji.emojize(":OK_hand:")))
async def send_request_to_dialog(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    text = "Новая квитанция\n" \
           f"ФИО ребенка: {data['username']}\n"\
           f"Класс и форма обучения: {data['grade']}\n"\
           f"Тип платежа: {data['type_payment']}\n"
    try:
        await bot.send_photo(CHANEL_ID, photo=data['doc'], caption=text)
        await message.answer("Квитанция сохранена!", reply_markup=chs_child())
    except aiogram.exceptions.TelegramBadRequest:
        try:
            await bot.send_document(CHANEL_ID, document=data['doc'], caption=text)
            await message.answer("Квитанция сохранена!", reply_markup=chs_child())
        except aiogram.exceptions.TelegramBadRequest:
            await message.answer("Не удалось сохранить квитанцию. Попробуйте позже или напишите администратору. Спасибо!")
    await state.clear()


@router.message(Send_Payment.send_que, Text(text="Заполнить заново" + emoji.emojize(":cross_mark_button:")))
async def request_again(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Введите ФИО ребенка", reply_markup=chs_child())
    await state.set_state(Send_Payment.name)
