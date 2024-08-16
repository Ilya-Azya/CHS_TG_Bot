import configparser

from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import types, Bot, F
from main import UserState
from aiogram.fsm.context import FSMContext
from keyboards.for_questions import not_for_child_chs, type_of_contact_req, manager_contact

router = Router()

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')

CHANEL_ID = config.get('CHS_Bot', 'chs_id')


@router.callback_query(Text(text="Оставить заявку"))
async def send_request(message: types.CallbackQuery, state: FSMContext):
  await message.message.reply(
      "*Присоединяйтесь к нам сегодня!*\n" \
      "Напишите свои данные, и мы свяжемся с Вами в течение часа.\n" \
      "Ваши данные ни при каких обстоятельствах не будут переданы третьим лицам.",
      parse_mode="Markdown"
  )
  await message.message.answer("Введите ваше *имя*", parse_mode="Markdown")
  await message.answer()
  await state.set_state(UserState.name)


@router.message(Text(text="Оставить заявку"))
async def send_request(message: Message, state: FSMContext):
  await message.reply(
      "*Присоединяйтесь к нам сегодня!*\n" \
      "Напишите свои данные, и мы свяжемся с Вами в течение часа.\n" \
      "Ваши данные ни при каких обстоятельствах не будут переданы третьим лицам.",
      parse_mode="Markdown"
  )
  await message.answer("Введите ваше *имя*", parse_mode="Markdown")
  await state.set_state(UserState.name)


@router.message(UserState.name)
async def get_username(message: Message, state: FSMContext):
  await state.update_data(username=message.text)
  await message.answer("Отлично! Введите удобный вид связи",
                       reply_markup=type_of_contact_req())
  await state.set_state(UserState.type_contact)


@router.message(UserState.type_contact, Text(text="Telegram"))
async def get_type_cont(message: Message, state: FSMContext):
  await state.update_data(type_contact=message.text)
  await message.answer(
    "Супер! Теперь введите ваш номер телефона, привязанный к Telegram",
    reply_markup=ReplyKeyboardRemove)
  await state.set_state(UserState.number)


@router.message(UserState.type_contact, Text(text="Viber"))
async def get_type_cont(message: Message, state: FSMContext):
  await state.update_data(type_contact=message.text)
  await message.answer(
    "Супер! Теперь введите ваш номер телефона, привязанный к Viber",
    reply_markup=ReplyKeyboardRemove)
  await state.set_state(UserState.number)


@router.message(UserState.type_contact, Text(text="WhatsApp"))
async def get_type_cont(message: Message, state: FSMContext):
  await state.update_data(type_contact=message.text)
  await message.answer(
    "Супер! Теперь введите ваш номер телефона, привязанный к WhatsApp",
    reply_markup=ReplyKeyboardRemove)
  await state.set_state(UserState.number)


@router.message(UserState.number)
async def get_number(message: Message, state: FSMContext):
  ms = message.text
  flag_er = False
  if not (ms[0] == '+' and len(ms) >= 6
          and len(ms) <= 19) and not (len(ms) >= 5 and len(ms) <= 18):
    await message.reply(
      "Введенный номер не соответствует стандартной длине\nПопробуйте еще раз")
    await state.set_state(UserState.number)
  else:
    for char in ms:
      if char in "+1234567890":
        continue
      else:
        flag_er = True
    if flag_er:
      await message.reply(
        "Введенный номер не соответствует страндартной форме\nПопробуйте еще раз"
      )
      await state.set_state(UserState.number)
    else:
      await state.update_data(numbers=message.text)
      data = await state.get_data()
      await state.set_state(UserState.send_question)
      await message.answer(
          "_Проверьте правильность данных_\n" \
          f"Ваше имя: {data['username']}\n" \
          f"Удобный способ связи: {data['type_contact']}\n" \
          f"Номер телефона: {data['numbers']}",
          parse_mode="Markdown",
          reply_markup=ReplyKeyboardMarkup(
              keyboard=[
                  [
                      KeyboardButton(text="Все верно"),
                      KeyboardButton(text="Заполнить заново")
                  ]
              ],
              resize_keyboard=True,
          ),
      )


@router.message(UserState.send_question, Text(text="Все верно"))
async def send_request_to_dialog(message: Message, state: FSMContext,
                                 bot: Bot):
  data = await state.get_data()
  text = "*Новая заявка от Бота*\n" \
         f"_Имя:_ *{data['username']}*\n" \
         f"_Тип связи:_ *{data['type_contact']}*\n" \
         f"_Номер телефона:_ *{data['numbers']}*\n" \
         f"_Username пользователя:_ @*{message.from_user.username}*"
  await bot.send_message(CHANEL_ID, text, parse_mode="Markdown")
  await message.answer(
    "Заявка отправлена!\nЕсли ваш аккаунт скрыт, наш менеджер не сможет с вами свзяаться.\nВы можете самостоятельно ему написать",
    reply_markup=manager_contact(),
  )
  await message.answer("Чем еще я могу вам помочь?",
                       reply_markup=not_for_child_chs())
  await state.clear()


@router.message(UserState.send_question, Text(text="Заполнить заново"))
async def request_again(message: Message, state: FSMContext):
  await state.clear()
  await message.answer("Введите ваше имя", reply_markup=not_for_child_chs())
  await state.set_state(UserState.name)
