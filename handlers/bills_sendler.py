from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import get_yes_no_kb, chs_child, format_learn, bills, bill_poland_send

router = Router()


@router.callback_query(Text(text="bill_RB"))
async def send_RB_Bill(callback: types.CallbackQuery):
    msg = "*Номер счета:*\nBY46ALFA3014308QV50050270000\n*Владелец счета:*\nVialichka Pavel"
    await callback.message.answer(msg, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(Text(text="bill_Pol"))
async def send_PL_Bill(callback: types.CallbackQuery):
    msg = "Выберите валюту"
    await callback.message.answer(msg, parse_mode="Markdown", reply_markup=bill_poland_send())
    await callback.answer()

@router.callback_query(Text(text="bill_Pol_eu"))
async def send_PL_Bill(callback: types.CallbackQuery):
    msg_eur = "_Счет в евро_\n*Cambridge High School Oleksandr Velychko*\n_ul. Ks. J. Popiełuszki 35/17 21-100 Lubartów_\n_NIP 7142059030 tel. 572 208 698_\nPL65 1020 3206 0000 8102 0175 0876\n*Банк PKO BP*\n*SWIFT: BPKOPLPW*"
    await callback.message.answer(msg_eur, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(Text(text="bill_Pol_zl"))
async def send_PL_Bill(callback: types.CallbackQuery):
    msg_zlt = "_Счет в злотых_\n*Cambridge High School Oleksandr Velychko*\n_ul. Ks. J. Popiełuszki 35/17 21-100 Lubartów_\n_NIP 7142059030 tel. 572 208 698_\nPL87 1020 3206 0000 8102 0175 0868\n*Банк PKO BP*\n*SWIFT: BPKOPLPW*"
    await callback.message.answer(msg_zlt, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(Text(text="bill_Montenegro"))
async def send_MNE_Bill(callback: types.CallbackQuery):
    msg = "*CHS-ONLINE doo*\n*RB 51066548; RIB 03476057*\n_Adresa: Poslovni Centar Kula A, BSC Bar_\n575-0000000001733-64\n*Банк Ziraat bank*\n*SWIFT: TCZBMEPGXXX*"
    await callback.message.answer(msg, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(Text(text="bill_USA"))
async def send_USA_Bill(callback: types.CallbackQuery):
    msg = "*Bank of America*\n_466015137104 Hide Account number_\n*SWIFT: BOFAUS3N*"
    await callback.message.answer(msg, parse_mode="Markdown")
    await callback.answer()
