from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.for_questions import coast_type, contacts_chs, go_to_dogov, go_to_admin, faq_menu, req_test, kate_contact

router = Router()


@router.message(Text(text="Частые вопросы"))
async def faq(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Ниже приведены основные выпросы и ответы на них\n\n" \
        "Вы так же всегда можете задать свой вопрос нашему *администратору*",
        parse_mode="Markdown",
        reply_markup=faq_menu()
    )


@router.callback_query(Text(text="faq_1"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Да! Мы принимаем учеников круглый год. Для зачисления к нам достаточно оформить заявку и с вами свяжется наш менеджер",
        parse_mode="Markdown",
        reply_markup=req_test()
    )
    await callback.answer()


@router.callback_query(Text(text="faq_2"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Выберите формат обучения",
        reply_markup=coast_type()
    )
    await callback.answer()


@router.callback_query(Text(text="faq_3"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Чтобы вам было проще определиться с зачислением, мы предлагаем посетить два бесплатных пробных дня." \
        "В эти дни Ваш ребенок посетит все уроки, пообщается с учителями, будущими одноклассниками и составит свое мнение о нашей школе!" \
        "Для записи на бесплатные пробные дни необходимо заполнить заявку.",
        reply_markup=req_test()
    )
    await callback.answer()


@router.callback_query(Text(text="faq_4"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Для записи на бесплатные пробные дни вам необходимо оставить заявку",
        reply_markup=req_test()
    )
    await callback.answer()


@router.callback_query(Text(text="faq_5"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "По окончании 12 класса ваш ребенок получит два документа: диплом об окончании школы и транскрипт (Документ, который содержит годовые отметки за 9 - 12 классы, заработанные кредиты, отметка за поведение и рейтинг ребенка в классе).",
    )
    await callback.answer()


@router.callback_query(Text(text="faq_6"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Если вы попали в ситуацию, когда ребенок не посещал школу некоторое время перед зачислением к нам," \
        " и у него не аттестована одна или несколько четвертей, без которых его нельзя аттестовать за год," \
        " необходимо записаться на контрольные работы по всем неаттестованным предметам. " \
        "Данные контрольные работы будут содержать задания за предыдущую(-ии) четверть. Полученная отметка пойдет в журнал." \
        "\nОбратите внимание, что данная процедура платная — 15 евро за 1 предмет.",
    )
    await callback.answer()


@router.callback_query(Text(text="faq_7"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Несмотря на то, что мы зарегистрированы в США," \
        " Cambridge High School нацелена на обучение русскоговорящих детей по всему Миру." \
        " Поэтому весь процесс обучения идет на русском языке! ",
    )
    await callback.answer()


@router.callback_query(Text(text="faq_8"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "С 2023 года в Cambridge High School появились предметы по выбору," \
        " то есть вашему ребенку предложат группы предметов из которых необходимо выбрать один," \
        " который он будет изучать с группой детей, которые выбрали такую же дисциплину." \
        " Например, вы самостоятельно выбираете второй иностранный язык.",
    )
    await callback.answer()


@router.callback_query(Text(text="faq_9"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        " За основу нашей учебной программы взята программа СНГ, по которой сейчас учатся в Украине, России и Беларуси." \
        " Однако, наша команда учителей на своих кафедрах адаптируют, улучшают и модернизирует свои предметы. Кроме того," \
        " некоторые дисциплины претерпели достаточно серьёзные изменения, например, география и история государства. География" \
        " идет с 5 до 7 класса, после чего География сливается с экономикой и историей права в теоретический предмет — Бизнес и право," \
        " который идет два года (8 - 9 класс). После прохождения теоретического курса, он трансформируется в практический — основы предпринимательской" \
        " деятельности (10 - 12 класс). На этом предмете дети практикуются применять полученные знания на практике, открыв свой собственный проект." \
        "Информатику мы изучаем на более глубоком уровне, именно поэтому она получила название Программирование." \
        "Русский язык и литература покинули учебную программу 10 - 12 классов в привычном для нас понимании, мы отошли от регулярных заданий," \
        " вечного тренинга грамматики через банальные упражнения. Мы объединили русский язык и литературу в один предмет. Теперь в старших классах дети" \
        " будут изучать язык на основе произведений мировых писателей и их произведений, а также через написание эссе, проведения дебатов и уроки рассуждения." \
        " Все это позволяет раскрывать творческий потенциал, помогает детям научиться формулировать свои мысли как устно, так и письменно.",
    )
    await callback.answer()


@router.callback_query(Text(text="faq_10"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "*Online обучение* — максимально приближен к очному формату. Уроки проходят в режиме реального времени на платформе ZOOM,"\
        " что означает, что дети и учитель вместе подключаются к уроку. Такой формат позволяет детям задавать вопросы учителю,"\
        " общаться между собой и не чувствовать себя одиноко за экраном. В этом формате будут классные работы, домашние, контрольные,"\
        " самостоятельные. Никаких записей уроков, все в живую!"\
        "\n*Homeschool* - это домашнее обучение, когда вы, как родитель, самостоятельно занимаетесь обучением вашего ребенка."\
        " Мы предоставим вам план, в котором прописано, что ребенок должен освоить за учебный год и рекомендуемую литературу."\
        " Преимущество в том, что способ обучения вы выбираете самостоятельно. Качество знаний проверяется посредством итоговой"\
        " аттестации, которая проводится 2 раза в год в 6 - 12 классах и 1 раз в год в 1 - 5 классах.",
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(Text(text="faq_11"))
async def ans_faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Да! Наш консультант по поступлении — Екатерина Александровна, с радостью поможет вам."
        " Она поможет вам определиться с выбором университета, специальности и свяжется с выбранными"
        " вузами и/или университетами, колледжами, узнает их условия поступления, стоимость, поможет в"
        " подготовке и оформлении необходимых для поступления документов.",
        reply_markup=kate_contact()
    )
    await callback.answer()


@router.message(Text(text="Мы в интернете"))
async def faq(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Будьте в курсе новостей:",
        reply_markup=contacts_chs()
    )


@router.message(Text(text="Порядок зачисления"))
async def faq(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "Для того, чтобы к нам присоединиться вам *необходимо:*\n" \
        "_1. Ознакомиться с договором публичной оферты на нашем сайте\n" \
        "2. Заполнить заявление, прикрепив к нему основные документы\n" \
        "3. Оплатить вступительный взнос\n" \
        "4. Отправить квитанцию об оплате мне или администратору, который с вами свяжется\n" \
        "5. Вступить в канал школы и канал класса\n" \
        "6. Оплатить один месяц обучения и прислать квитанцию мне или администратору\n" \
        "7. Приступить к обучению_",
        parse_mode="Markdown",
        reply_markup=go_to_dogov()
    )


@router.message(Text(text="Контакты"))
async def faq(message: Message, state: FSMContext):
    await state.clear()
    await message.reply(
        "По вопросам обучение в _Cambrige High School_ обращайтесь к *Manager.*\n" \
        "По вопросам _помощи в поступлении_ обращайтесь к *Guidance counselor.*",
        parse_mode="Markdown",
        reply_markup=go_to_admin()
    )
