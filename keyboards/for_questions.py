from aiogram import types
from aiogram.filters import callback_data
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

import emoji


def start_main() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Начать работу",
        callback_data="/start"
    ))
    return kb.as_markup()


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да" + emoji.emojize(":OK_hand:"))
    kb.button(text="Нет" + emoji.emojize(":cross_mark_button:"))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def chs_child() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Оплата")
    kb.button(text="Учебный процесс")
    # kb.button(text="Психолог")
    kb.button(text="Дополнительные занятия")
    kb.button(text="Ничего из этого")
    kb.button(text="Наши telegram-каналы")
    kb.button(text="Назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите что вас интересует")


def tel_canals() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Telegram-канал школы",
        url="https://t.me/+UzXFZ0YVChVlYTE0"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Telegram-канал класса",
        callback_data="tel_grades"
    ))
    return kb.as_markup()


def payment_kb_choice() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Отправить квитанцию")
    kb.button(text="Узнать стоимость")
    kb.button(text="Реквизиты")
    kb.button(text="Другой вопрос")
    kb.button(text="Вернуться назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def format_learn() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Online")
    kb.button(text="Homeshcool")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def bills() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Беларусь" + emoji.emojize(":Belarus:"), callback_data="bill_RB"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Польша" + emoji.emojize(":Poland:"), callback_data="bill_Pol"
    ))
    kb.add(types.InlineKeyboardButton(
        text="США" + emoji.emojize(":United_States:"), callback_data="bill_USA"
    ))
    inline_kb = types.InlineKeyboardButton(
        text="Черногория" + emoji.emojize(":Montenegro:"), callback_data="bill_Montenegro"
    )
    kb.row(inline_kb)
    return kb.as_markup()


def bill_poland_send() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Счет в злотых", callback_data="bill_Pol_eu"))
    kb.add(types.InlineKeyboardButton(text="Счет в евро", callback_data="bill_Pol_zl"))
    return kb.as_markup()


def coast_type() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Online " + emoji.emojize(":desktop_computer:"),
        callback_data="coast_online"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Homeschool " + emoji.emojize(":derelict_house:"),
        callback_data="coast_IP"
    ))
    return kb.as_markup()


def coast_online() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    inline_kb_elem = types.InlineKeyboardButton(text="Начальная школа (1-5 класс)", callback_data="coast_elementary")
    inline_kb_midl = types.InlineKeyboardButton(text="Средняя школа (6-8 класс)", callback_data="coast_middle")
    inline_kb_high = types.InlineKeyboardButton(text="Старшая школа (9-12 класс)", callback_data="coast_high")
    kb.row(inline_kb_elem)
    kb.row(inline_kb_midl)
    kb.row(inline_kb_high)
    return kb.as_markup()


def psyh_questions() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Информация")
    kb.button(text="Связаться с психологом")
    kb.button(text="Канал психолога")
    kb.button(text="Вернуться назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def psyh_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    inline_kb_1 = types.InlineKeyboardButton(text="Мне нужна помощь психолога", callback_data="contact_psyh")
    inline_kb_2 = types.InlineKeyboardButton(text="Сами вы психи!", callback_data="back_main_chs")
    kb.row(inline_kb_1)
    kb.row(inline_kb_2)
    return kb.as_markup()


def learn_proc_questions() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Электронный журнал", callback_data="el_journal")
    kb.button(text="Учебные пособия")
    kb.button(text="Пересдачи")
    kb.button(text="Правила CHS")
    kb.button(text="Вернуться назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def grade_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="4",
        url="https://docs.google.com/spreadsheets/d/1qbqgNgNYSExG79_Ys9_lqHS3A-zgzuXP1rB9atLh_s4/edit?usp=sharing_"
    ))
    kb.add(types.InlineKeyboardButton(
        text="5",
        url="https://docs.google.com/spreadsheets/d/1qbqgNgNYSExG79_Ys9_lqHS3A-zgzuXP1rB9atLh_s4/edit?usp=sharing_"
    ))
    kb.add(types.InlineKeyboardButton(
        text="6",
        url="https://docs.google.com/spreadsheets/d/1ikdHf4qodAdMc20mm4VnlePu8Xd7eYyyJ0kTs98Lm-A/edit?usp=sharing"
    ))
    kb.add(types.InlineKeyboardButton(
        text="7",
        url="https://docs.google.com/spreadsheets/d/15Q64_P8SrZGNFxfYyHmfUq_cmmeEYShHt-W6Livb5bY/edit?usp=sharing"
    ))
    kb.add(types.InlineKeyboardButton(
        text="8",
        url="https://docs.google.com/spreadsheets/d/1qOOfr929kPytIjqu1CIgqqNgCR6z5V8s9vKTMrBeZuc/edit?usp=sharing"
    ))
    kb_inline_8 = types.InlineKeyboardButton(
        text="9",
        url="https://docs.google.com/spreadsheets/d/1E3VNPW24-KlvNtPr7CdQnEdzaREOw-tCLYLLmhpJ-y8/edit?usp=sharing"
    )
    kb.row(kb_inline_8)
    kb.add(types.InlineKeyboardButton(
        text="10",
        url="https://docs.google.com/spreadsheets/d/1S5eOnYEWp9uoKpX6EuMYMqJUArg90u6g0mkLXR-O1gY/edit?usp=sharing"
    ))
    kb.add(types.InlineKeyboardButton(
        text="11",
        url="https://docs.google.com/spreadsheets/d/1zOZfkoO_JveRxu_alFHXGRGJf-01X4B5KqPsYuvJ9xU/edit?usp=sharing"
    ))
    kb.add(types.InlineKeyboardButton(
        text="12",
        url="https://docs.google.com/spreadsheets/d/1vg0SaJ-Lj15OA5yEmA376U0I9Vooix_8cHPbbOJFv3c/edit?usp=sharing"
    ))
    return kb.as_markup()


def book_grade_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="1-5", url="https://mega.nz/folder/HsYwHSRS#Br-7k2xFHo-tH2pXL084Lw"))
    kb.add(types.InlineKeyboardButton(text="6", url="https://mega.nz/folder/q8IXhaCQ#o5SKR-USzA4qujI4gtNvTA"))
    kb.add(types.InlineKeyboardButton(text="7", url="https://mega.nz/folder/D0YR2CCQ#xHqhkJ0LbHeBbTaaOw14Rw"))
    kb.add(types.InlineKeyboardButton(text="8", url="https://mega.nz/folder/WshQWaLa#FKQIOzu8NlV_bqzwpUGy_A"))
    inline_kb_8 = types.InlineKeyboardButton(text="9", url="https://mega.nz/folder/74hGzS5I#SAIms9_cZgcsosUs9L9BlQ")
    kb.row(inline_kb_8)
    kb.add(types.InlineKeyboardButton(text="10", url="https://mega.nz/folder/v1oAxLYC#MnAqo5QQc9_dAzWqAHyj4Q"))
    kb.add(types.InlineKeyboardButton(text="11", url="https://mega.nz/folder/H8owHbIA#Fe_ga4GTw-K1S5v6Q43jSg"))
    kb.add(types.InlineKeyboardButton(text="12", url="https://mega.nz/folder/a8gxhYgS#LEMDXuK6pF_2NMAHvCMrfw"))
    return kb.as_markup()


def retake_info() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Основная информация",
        callback_data="main_info_retake"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Реквизиты",
        callback_data="retake_bills"
    ))
    return kb.as_markup()


def retake_info_bill() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Реквизиты" + emoji.emojize(":money_with_wings:"),
                                      callback_data="retake_bills"))
    return kb.as_markup()


def save_bill() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Отправить подтверждение платежа", callback_data="save_bill"))
    return kb.as_markup()


def extra_classes() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Основная информация")
    kb.button(text="Стоимость занятий")
    kb.button(text="Запись на занятия")
    kb.button(text="Другой вопрос")
    kb.button(text="Вернуться назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def registr_extra() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Запись на занятия", callback_data="registr_extra"))
    return kb.as_markup()


def admins() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Администраторы", callback_data="admins"))
    return kb.as_markup()


def not_for_child_chs() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Частые вопросы")
    kb.button(text="Мы в интернете")
    kb.button(text="Порядок зачисления")
    kb.button(text="Контакты")
    kb.button(text="Оставить заявку")
    kb.button(text="Назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def leave_req() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Перейти на сайт", url="https://chschool.eu/"))
    return kb.as_markup()


def contacts_chs() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Наш сайт", url="https://chschool.eu/"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Instagram", url="https://www.instagram.com/cambridge_high_school/"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Telegram", url="https://t.me/chsmeneger"
    ))
    return kb.as_markup()


def go_to_dogov() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Договор", url="https://chschool.eu/dogovor"))
    return kb.as_markup()


def go_to_admin() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Manager", url="https://t.me/chsmeneger"))
    inline_kb = types.InlineKeyboardButton(text="Guidance counselor", url="https://t.me/Guidance_counselor")
    kb.row(inline_kb)
    return kb.as_markup()


def tel_canal_grades() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Online " + emoji.emojize(":desktop_computer:"),
        callback_data="tel_canals_online"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Homeschool " + emoji.emojize(":derelict_house:"),
        callback_data="tel_canals_IP"
    ))
    return kb.as_markup()


def grades_online_tel_canals() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    # kb.add(types.InlineKeyboardButton(text="3 класс", url="https://t.me/+P-SdJmPSHJ8zNzE0"))
    # kb.add(types.InlineKeyboardButton(text="4 класс", url="https://t.me/+P-SdJmPSHJ8zNzE0"))
    # kb.add(types.InlineKeyboardButton(text="5 класс", url="https://t.me/+YiQhieNEdixiYTM0"))
    # kb.add(types.InlineKeyboardButton(text="6 класс", url="https://t.me/+sKoUuoTTfXA4ZmM8"))
    # kb.add(types.InlineKeyboardButton(text="7 класс", url="https://t.me/+aJXLCwS_Yv1hZTk0"))
    # inline_kb_8 = types.InlineKeyboardButton(text="8 класс", url="https://t.me/+K7l7IwGF-ys5NzQ0")
    # kb.row(inline_kb_8)
    # kb.add(types.InlineKeyboardButton(text="9 класс", url="https://t.me/+iXYx2P3-l3dlYTE0"))
    # kb.add(types.InlineKeyboardButton(text="10 класс", url="https://t.me/+ZwZAr23jJS0zODA0"))
    # kb.add(types.InlineKeyboardButton(text="11 класс", url="https://t.me/+p0DkHT7DUdo3OWE0"))
    kb.add(types.InlineKeyboardButton(text="Администратор Online", url="https://t.me/jaffast2"))
    return kb.as_markup()


def grades_ip_tel_canals() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    # kb.add(types.InlineKeyboardButton(text="1 класс", url="https://t.me/+8Oj3H90pRaBhZDg0"))
    # kb.add(types.InlineKeyboardButton(text="2 класс", url="https://t.me/+qPaPJJLAdHNmMGNk"))
    # kb.add(types.InlineKeyboardButton(text="3 класс", url="https://t.me/+krJ62MLhLAg4NTU8"))
    # kb.add(types.InlineKeyboardButton(text="4 класс", url="https://t.me/+1zdZvpSGJ5dhMjc0"))
    # inline_kb_5 = types.InlineKeyboardButton(text="5 класс", url="https://t.me/+IywmCnj_TPg3MzY0")
    # kb.row(inline_kb_5)
    # kb.add(types.InlineKeyboardButton(text="6 класс", url="https://t.me/+CWROn2rsrLY0ODI0"))
    # kb.add(types.InlineKeyboardButton(text="7 класс", url="https://t.me/+8RQyOKcGJnY5ZTg8"))
    # kb.add(types.InlineKeyboardButton(text="8 класс", url="https://t.me/+LGuQloTrvrU4NmNk"))
    # inline_kb_9 = types.InlineKeyboardButton(text="9 класс", url="https://t.me/+BHTH1so_0xo4YWM8")
    # kb.row(inline_kb_9)
    # kb.add(types.InlineKeyboardButton(text="10 класс", url="https://t.me/+7RMzWC1VMu5iOGU0"))
    # kb.add(types.InlineKeyboardButton(text="11 класс", url="https://t.me/+LIDRxWyjqjE1YTNk"))
    # kb.add(types.InlineKeyboardButton(text="12 класс", url="https://t.me/+MBu7u8wQvAdjM2Y0"))
    kb.add(types.InlineKeyboardButton(text="Администратор Homeschool", url="https://t.me/mmalses"))
    return kb.as_markup()


def faq_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text="Можно перейти к вам посреди учебного года?", callback_data="faq_1"))
    inline_kb_2 = types.InlineKeyboardButton(text="Сколько стоит обучение?", callback_data="faq_2")
    inline_kb_3 = types.InlineKeyboardButton(text="Что из себя представляют пробные дни?", callback_data="faq_3")
    inline_kb_4 = types.InlineKeyboardButton(text="Как попасть на бесплатные пробные дни?",
                                             callback_data="faq_4")
    inline_kb_5 = types.InlineKeyboardButton(text="Какие документы получит ребенок по окончании школы?",
                                             callback_data="faq_5")
    inline_kb_6 = types.InlineKeyboardButton(text="Что делать если ребенок не аттестован за четверть?",
                                             callback_data="faq_6")
    inline_kb_7 = types.InlineKeyboardButton(text="На каком языке идет обучение?", callback_data="faq_7")
    inline_kb_8 = types.InlineKeyboardButton(text="Что такое предмет по выбору?", callback_data="faq_8")
    inline_kb_9 = types.InlineKeyboardButton(text="Какие особенности вашей учебной программы?", callback_data="faq_9")
    inline_kb_10 = types.InlineKeyboardButton(text="Чем отличается Online обучение от Homeschool?",
                                              callback_data="faq_10")
    inline_kb_11 = types.InlineKeyboardButton(text="Вы помогаете с поступлением в университет?", callback_data="faq_11")
    kb.row(inline_kb_2)
    kb.row(inline_kb_3)
    kb.row(inline_kb_4)
    kb.row(inline_kb_5)
    kb.row(inline_kb_6)
    kb.row(inline_kb_7)
    kb.row(inline_kb_8)
    kb.row(inline_kb_9)
    kb.row(inline_kb_10)
    kb.row(inline_kb_11)
    return kb.as_markup()


def send_report() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="created by JS", url="https://t.me/jaffast2"
    ))
    return kb.as_markup()


def for_dif() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Помощь", callback_data="/help"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Cтарт", callback_data="/start"
    ))
    return kb.as_markup()


def yes_no_request() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Все верно", callback_data="yes_req"
    ))
    kb.add(types.InlineKeyboardButton(
        text="Заполнить заново", callback_data="no_req"
    ))
    return kb.as_markup()


def req_test() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Оставить заявку",
        callback_data="Оставить заявку"
    ))
    return kb.as_markup()


def kate_contact() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    inline_kb = types.InlineKeyboardButton(text="Екатерина Александровна", url="https://t.me/Guidance_counselor")
    kb.row(inline_kb)
    return kb.as_markup()


def manager_contact() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    inline_kb = types.InlineKeyboardButton(text="Manager", url="https://t.me/chsmeneger")
    kb.row(inline_kb)
    return kb.as_markup()


def type_of_contact_req() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Telegram")
    kb.button(text="Viber")
    kb.button(text="WhatsApp")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")
