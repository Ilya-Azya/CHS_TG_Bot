from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import registr_extra, admins, format_learn
from aiogram import types

router = Router()


@router.message(Text(text="Запись на занятия"))
async def back_start(message: Message):
    await message.reply(
        "Для записи ответьте на несколько вопросов 👇\n\nhttps://forms.gle/9nBs2wsNHKF7tCQR7"
    )


@router.message(Text(text="Основная информация"))
async def main_info_extra(message: Message):
    await message.reply(
        "Наши учителя готовы предложить вам факультативы и дополнительные занятия по всем _основным предметам_ во второй половине дня, два раза в неделю, очно и онлайн.\n\nЕсли у вас желание или необходимость - нажмите 'Запись на занятия'",
        parse_mode="Markdown",
        reply_markup=registr_extra()
    )

@router.callback_query(Text(text="registr_extra"))
async def registration_send(callback: types.CallbackQuery):
    await callback.message.reply(
        "Для записи вам необходимо пройти небольшой опрос по ссылке ниже\n\nhttps://forms.gle/9nBs2wsNHKF7tCQR7"
    )
    await callback.answer()

@router.message(Text(text="Стоимость занятий"))
async def cost_extra(message: Message):
    await message.reply(
        "Стоимость групповых занятий зависит от _комплектации группы_:\n"\
        "*4+* человека в группе - *35€* в месяц _(8 занятий)_\n"\
        "*1-3* человека в группе - стоимость уточняйте у _администраторов_\n\n"\
        "Стоимость _индивидуальных занятий_ учтоняется лично у учителя\n\n"\
        "_Дополнительную информацию_ можете узнать у *администраторов* по _кнопке ниже_",
        parse_mode="Markdown",
        reply_markup=admins()
    )

@router.callback_query(Text(text="admins"))
async def admins_info_send(callback: types.CallbackQuery):
    await callback.message.reply(
        "Выберите формат обучения",
        reply_markup=format_learn()
    )
    await callback.answer()