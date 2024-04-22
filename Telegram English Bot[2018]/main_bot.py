import time

import selenium
import telebot
import cfg
import kb
import funk
from selenium import webdriver

bot = telebot.TeleBot(cfg.TOKEN)


# Начальная панель
@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('mn'))
def process_callback_keyboard_menu(callback_query):
    callback_kb_menu = callback_query.data[-1]
    if callback_kb_menu.isdigit():
        callback_kb_menu = int(callback_kb_menu)
    if callback_kb_menu == 1:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_theory)
    elif callback_kb_menu == 2:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    elif callback_kb_menu == 3:
        bot.answer_callback_query(callback_query.id)
        google_input(callback_query)
    elif callback_kb_menu == 4:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        ex_welcome(callback_query)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Теория'
@bot.callback_query_handler(func=lambda c: True and c.data.startswith('thr'))
def process_callback_keyboard_theory(callback_query):
    callback_kb_thr = callback_query.data[-1]
    if callback_kb_thr.isdigit():
        callback_kb_thr = int(callback_kb_thr)
    if callback_kb_thr == 1:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_modal)
    elif callback_kb_thr == 2:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_appearance)
    elif callback_kb_thr == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Gerund:\n')
        funk.photo_gerund(callback_query)
    elif callback_kb_thr == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Participle:\n')
        funk.photo_participle(callback_query)
    elif callback_kb_thr == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Future in the Past:\n')
        funk.photo_future(callback_query)
    elif callback_kb_thr == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_menu)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('ex'))
def process_callback_keyboard_exercise(callback_query):
    callback_kb_ex = callback_query.data[-1]
    if callback_kb_ex.isdigit():
        callback_kb_ex = int(callback_kb_ex)
    if callback_kb_ex == 1:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_modal_ex)
    elif callback_kb_ex == 2:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_participle_ex)
    elif callback_kb_ex == 3:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_passive_ex)
    elif callback_kb_ex == 4:
        bot.answer_callback_query(callback_query.id)
        funk.exercise_gerund1(callback_query)
    elif callback_kb_ex == 5:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_translate_ex)
    elif callback_kb_ex == 6:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_text_ex)
    elif callback_kb_ex == 7:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_word_ex)
    elif callback_kb_ex == 8:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_unkbook_ex)
    elif callback_kb_ex == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_menu)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Modal Verbs' в 'Теория'
@bot.callback_query_handler(func=lambda c: c.data.startswith('mdl'))
def process_callback_keyboard_modal(callback_query):
    callback_kb_mdl = callback_query.data[-1]
    if callback_kb_mdl.isdigit():
        callback_kb_mdl = int(callback_kb_mdl)
    if callback_kb_mdl == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Be to:\n')
        funk.photo_be_to(callback_query)
    elif callback_kb_mdl == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Can/Could:\n')
        funk.photo_can(callback_query)
    elif callback_kb_mdl == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'May/Might:\n')
        funk.photo_may(callback_query)
    elif callback_kb_mdl == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Must/Have to:\n')
        funk.photo_must(callback_query)
    elif callback_kb_mdl == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Shall/Will:\n')
        funk.photo_shall(callback_query)
    elif callback_kb_mdl == 6:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Would:\n')
        funk.photo_would(callback_query)
    elif callback_kb_mdl == 7:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Dare:\n')
        funk.photo_dare(callback_query)
    elif callback_kb_mdl == 8:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Theory Modal Verbs:\n')
        funk.modal_theory(callback_query)
    elif callback_kb_mdl == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_theory)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Appearance and Character' в 'Теория'
@bot.callback_query_handler(func=lambda c: c.data.startswith('app'))
def process_callback_keyboard_appearance(callback_query):
    callback_kb_app = callback_query.data[-1]
    if callback_kb_app.isdigit():
        callback_kb_app = int(callback_kb_app)
    if callback_kb_app == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Appearance:\n')
        funk.photo_appearance(callback_query)
    elif callback_kb_app == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Character:\n')
        funk.photo_character(callback_query)
    elif callback_kb_app == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_theory)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Modal Verbs' в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('mod'))
def process_callback_keyboard_modal(callback_query):
    callback_kb_mod = callback_query.data[-1]
    if callback_kb_mod.isdigit():
        callback_kb_mod = int(callback_kb_mod)
    if callback_kb_mod == 1:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужное упражнение:', reply_markup=kb.keyboard_beto_ex)
    elif callback_kb_mod == 2:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужное упражнение:', reply_markup=kb.keyboard_can_ex)
    elif callback_kb_mod == 3:
        bot.answer_callback_query(callback_query.id)
        funk.exercise_modal1(callback_query)
    elif callback_kb_mod == 4:
        bot.answer_callback_query(callback_query.id)
        funk.exercise_must1(callback_query)
    elif callback_kb_mod == 5:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужное упражнение:', reply_markup=kb.keyboard_shall_ex)
    elif callback_kb_mod == 6:
        bot.answer_callback_query(callback_query.id)
        funk.exercise_will1(callback_query)
    elif callback_kb_mod == 7:
        bot.answer_callback_query(callback_query.id)
        funk.exercise_dare1(callback_query)
    elif callback_kb_mod == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Be to/Have to' в Modal Verbs в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('bet'))
def process_callback_keyboard_beto(callback_query):
    callback_kb_bet = callback_query.data[-1]
    if callback_kb_bet.isdigit():
        callback_kb_bet = int(callback_kb_bet)
    if callback_kb_bet == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Be to (08.07.19):\n')
        funk.exercise_be_to1(callback_query)
    elif callback_kb_bet == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Be to (17.04.20):\n')
        funk.exercise_be_to2(callback_query)
    elif callback_kb_bet == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Be to/Have to (11.07.19):\n')
        funk.exercise_be_to3(callback_query)
    elif callback_kb_bet == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Be to/Have to (16.04.20):\n')
        funk.exercise_be_to4(callback_query)
    elif callback_kb_bet == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Be to/Have to (17.04.20):\n')
        funk.exercise_be_to5(callback_query)
    elif callback_kb_bet == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_modal_ex)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Can/May/Must' в Modal Verbs в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('can'))
def process_callback_keyboard_can(callback_query):
    callback_kb_can = callback_query.data[-1]
    if callback_kb_can.isdigit():
        callback_kb_can = int(callback_kb_can)
    if callback_kb_can == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Can (27.03.20):\n')
        funk.exercise_can1(callback_query)
    elif callback_kb_can == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Can/May (02.04.20):\n')
        funk.exercise_can2(callback_query)
    elif callback_kb_can == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Can/May (02.04.20) v.2:\n')
        funk.exercise_can3(callback_query)
    elif callback_kb_can == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Can/May/Must (09.04.20):\n')
        funk.exercise_can4(callback_query)
    elif callback_kb_can == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_modal_ex)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Shall/Will' в Modal Verbs в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('shall'))
def process_callback_keyboard_shall(callback_query):
    callback_kb_shall = callback_query.data[-1]
    if callback_kb_shall.isdigit():
        callback_kb_shall = int(callback_kb_shall)
    if callback_kb_shall == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Shall/Will (23.04.20):\n')
        funk.exercise_shall1(callback_query)
    elif callback_kb_shall == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Shall/Will (30.04.20):\n')
        funk.exercise_shall2(callback_query)
    elif callback_kb_shall == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_modal_ex)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Participle' в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('part'))
def process_callback_keyboard_participle(callback_query):
    callback_kb_part = callback_query.data[-1]
    if callback_kb_part.isdigit():
        callback_kb_part = int(callback_kb_part)
    if callback_kb_part == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Participle (04.11.19):\n')
        funk.exercise_participle1(callback_query)
    elif callback_kb_part == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Participle (04.11.19) v.2:\n')
        funk.exercise_participle2(callback_query)
    elif callback_kb_part == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Participle (07.11.19):\n')
        funk.exercise_participle3(callback_query)
    elif callback_kb_part == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Participle (13.11.19):\n')
        funk.exercise_participle4(callback_query)
    elif callback_kb_part == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Participle (01.12.19):\n')
        funk.exercise_participle5(callback_query)
    elif callback_kb_part == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Passive Voice' в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('pass'))
def process_callback_keyboard_passive(callback_query):
    callback_kb_pass = callback_query.data[-1]
    if callback_kb_pass.isdigit():
        callback_kb_pass = int(callback_kb_pass)
    if callback_kb_pass == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Passive Voice (01.11.18):\n')
        funk.exercise_passive1(callback_query)
    elif callback_kb_pass == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Passive Voice (18.02.19):\n')
        funk.exercise_passive2(callback_query)
    elif callback_kb_pass == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Translation' в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('trans'))
def process_callback_keyboard_translate(callback_query):
    callback_kb_trans = callback_query.data[-1]
    if callback_kb_trans.isdigit():
        callback_kb_trans = int(callback_kb_trans)
    if callback_kb_trans == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Translation (26.03.18):\n')
        funk.exercise_translate1(callback_query)
    elif callback_kb_trans == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Translation (05.01.19):\n')
        funk.exercise_translate2(callback_query)
    elif callback_kb_trans == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Translation (11.02.19):\n')
        funk.exercise_translate3(callback_query)
    elif callback_kb_trans == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Translation (24.07.19):\n')
        funk.exercise_translate4(callback_query)
    elif callback_kb_trans == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Translation (18.11.19):\n')
        funk.exercise_translate5(callback_query)
    elif callback_kb_trans == 6:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Translation (02.12.19):\n')
        funk.exercise_translate6(callback_query)
    elif callback_kb_trans == 7:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Translation (09.12.19):\n')
        funk.exercise_translate7(callback_query)
    elif callback_kb_trans == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Texts' в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('text'))
def process_callback_keyboard_texts(callback_query):
    callback_kb_text = callback_query.data[-1]
    if callback_kb_text.isdigit():
        callback_kb_text = int(callback_kb_text)
    if callback_kb_text == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Chocolate - Food of the Gods (17.01.19):\n')
        funk.exercise_text1(callback_query)
    elif callback_kb_text == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Cosmic Black Holes (21.01.19):\n')
        funk.exercise_text2(callback_query)
    elif callback_kb_text == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Model Teacher (25.02.19):\n')
        funk.exercise_text3(callback_query)
    elif callback_kb_text == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Text (18.03.19):\n')
        funk.exercise_text4(callback_query)
    elif callback_kb_text == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'A Lilac Bush (08.04.19):\n')
        funk.exercise_text5(callback_query)
    elif callback_kb_text == 6:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Meals (16.05.19):\n')
        funk.exercise_text6(callback_query)
    elif callback_kb_text == 7:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Have You Ever Been to Peru (26.03.20):\n')
        funk.exercise_text7(callback_query)
    elif callback_kb_text == 8:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Prairie Dog with Sweet Tooth Found on Farm (26.03.20):\n')
        funk.exercise_text8(callback_query)
    elif callback_kb_text == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Words' в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('word'))
def process_callback_keyboard_words(callback_query):
    callback_kb_word = callback_query.data[-1]
    if callback_kb_word.isdigit():
        callback_kb_word = int(callback_kb_word)
    if callback_kb_word == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Phrases (27.03.19):\n')
        funk.exercise_word1(callback_query)
    elif callback_kb_word == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Sentences (14.03.19):\n')
        funk.exercise_word2(callback_query)
    elif callback_kb_word == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Sentences (08.04.19):\n')
        funk.exercise_word3(callback_query)
    elif callback_kb_word == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Discussing Arrangements for a Party (08.04.19):\n')
        funk.exercise_word4(callback_query)
    elif callback_kb_word == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Put Word (21.03.20):\n')
        funk.exercise_word5(callback_query)
    elif callback_kb_word == 6:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Put Word (22.03.20):\n')
        funk.exercise_word6(callback_query)
    elif callback_kb_word == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Unknown Book' в 'Упражнения'
@bot.callback_query_handler(func=lambda c: c.data.startswith('unk'))
def process_callback_keyboard_unkbook(callback_query):
    callback_kb_unk = callback_query.data[-1]
    if callback_kb_unk.isdigit():
        callback_kb_unk = int(callback_kb_unk)
    if callback_kb_unk == 1:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.1,2,3 p.262 (31.07.18):\n')
        funk.exercise_unkbook1(callback_query)
    elif callback_kb_unk == 2:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.18,19 p.55 (22.10.18):\n')
        funk.exercise_unkbook2(callback_query)
    elif callback_kb_unk == 3:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.5,6 p.157 (05.11.18):\n')
        funk.exercise_unkbook3(callback_query)
    elif callback_kb_unk == 4:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.5,6 p.188 (05.11.18):\n')
        funk.exercise_unkbook4(callback_query)
    elif callback_kb_unk == 5:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.10,14 p.192 (18.11.18):\n')
        funk.exercise_unkbook5(callback_query)
    elif callback_kb_unk == 6:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.23 p.54 (27.12.18):\n')
        funk.exercise_unkbook6(callback_query)
    elif callback_kb_unk == 7:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.27,28 p.164 (27.12.18):\n')
        funk.exercise_unkbook7(callback_query)
    elif callback_kb_unk == 8:
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'ex.9 p.153 (16.05.20):\n')
        funk.exercise_unkbook8(callback_query)
    elif callback_kb_unk == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_exercise)
    else:
        bot.answer_callback_query(callback_query.id)


# Панель 'Работа с упражнениями'
@bot.callback_query_handler(func=lambda c: c.data.startswith('mex'))
def process_callback_keyboard_make_exercise(callback_query):
    global url
    callback_kb_mex = callback_query.data[-1]
    if callback_kb_mex.isdigit():
        callback_kb_mex = int(callback_kb_mex)
    if callback_kb_mex == 1:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        url = cfg.url_en
        ex_start(callback_query)
    elif callback_kb_mex == 2:
        bot.answer_callback_query(callback_query.id)
        url = cfg.url_ru
        ex_start(callback_query)
    elif callback_kb_mex == 0:
        bot.answer_callback_query(callback_query.id)
        bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        bot.send_message(callback_query.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_menu)
    else:
        bot.answer_callback_query(callback_query.id)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.delete_message(message.chat.id, message.message_id)
    print(message)
    bot.send_message(message.chat.id,
                     'Добро пожаловать!\n'
                     'Этот бот был создан как сборник материалов, а также упражнений.\n'
                     'По сути это мои конспекты.\n'
                     'ВНИМАНИЕ: Если фотографии не прогружаются, подождите, они загрузятся 😉\n'
                     'Для работы нажмите на /list.\n'
                     'Приятного использования!')
    with open('user_registration.txt', 'a') as user_agent:
        user_id = str(message.from_user.id)
        user_agent.write("id: " + user_id + " || ")
        user_agent.write("Username: " + str(message.from_user.username) + " || ")
        lastname = str(message.from_user.last_name)
        if str(message.from_user.last_name) == "None":
            lastname = ""
        user_agent.write("Name: " + str(message.from_user.first_name) + " " + str(lastname) + "\n")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, '/start - Начать работу с ботом\n'
                                      '/help - Узнать все функции бота\n'
                                      '/list - Открыть панель управления\n'
                                      '/clear - Очистить чат от сообщений\n'
                                      '/delete - Удалить сообщение\n'
                                      '/google - Использовать переводчик Google\n'
                                      '/ex - Панель для работы с упражнениями')


@bot.message_handler(commands=['users'])
def users_message(message):
    try:
        if str(message.from_user.id) == cfg.owner:
            with open('user_registration.txt', 'rt') as user_message:
                bot.send_message(message.from_user.id, user_message.read())
        else:
            bot.send_message(message.from_user.id, "You're not the owner!\nOnly owner can use this function!")
    except telebot.apihelper.ApiException:
        if str(message.from_user.id) == cfg.owner:
            bot.send_message(message.from_user.id, "Пустой список")
        else:
            bot.send_message(message.from_user.id, "You're not the owner!\nOnly owner can use this function!")


@bot.message_handler(commands=['google'], content_types=['text'])
def google_driver(message):
    global browser
    chromedriver = 'chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    google_input(message)


def google_input(message):
    sent = bot.send_message(message.from_user.id, 'Введите слово или фразу для перевода:\n'
                                                  'Или введите /exit для выхода из перевода')
    bot.register_next_step_handler(sent, google_message)


def google_message(message):
    if message.text == '/exit':
        bot.send_message(message.chat.id, 'Перевод остановлен')
        return
    phrase = message.text
    space = phrase.split()
    phrase = '%20'.join(space)
    try:
        bot.send_message(message.chat.id, "Ожидайте перевод...")
        browser.get(
            'https://translate.google.com/?source=gtx_c#auto/ru/' + str(phrase))
        send = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]')
        bot.delete_message(message.chat.id, message.message_id + 1)
        if send.text == phrase:
            bot.send_message(message.chat.id, "Вы ввели слово или предложение на том же языке!\nПопробуйте еще раз.")
            google_input(message)
        else:
            bot.send_message(message.chat.id, send.text)
    except selenium.common.exceptions.WebDriverException:
        bot.delete_message(message.chat.id, message.message_id + 1)
        bot.send_message(message.chat.id, 'Попробуйте еще раз!')
        google_input(message)


@bot.message_handler(commands=['ex'], content_types=['text'])
def ex_welcome(message):
    global browser
    bot.send_message(message.from_user.id, 'Добро пожаловать!\nЭтот раздел сделан для быстрой и удобной работы '
                                           'с упражнениями.\nВыберете, что вы хотите сделать:',
                     reply_markup=kb.keyboard_make_ex)
    chromedriver = 'chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)


def ex_start(message):
    new = bot.send_message(message.from_user.id, 'Введите слово или предложение для перевода.\n'
                                                 'Или введите /exit для выхода из перевода')
    bot.register_next_step_handler(new, translate)


def translate(message):
    if message.text == '/exit':
        bot.send_message(message.chat.id, 'Перевод остановлен')
        send_translate(message)
        with open('EnglishText/make_ex.txt', 'w'):
            pass
        return
    phrase = message.text
    space = phrase.split()
    phrase = '%20'.join(space)
    try:
        bot.send_message(message.chat.id, "Ожидайте перевод...")
        browser.get(url + str(phrase))
        send = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]')
        bot.delete_message(message.chat.id, message.message_id + 1)
        if send.text == phrase:
            bot.send_message(message.chat.id, "Вы ввели слово или предложение на том же языке!\nПопробуйте еще раз.")
            ex_start(message)
        else:
            nstep = bot.send_message(message.chat.id, 'Записано! Хотите продолжить или закончить и сохранить перевод?',
                                     reply_markup=kb.keyboard_save)
            with open('EnglishText/make_ex.txt', 'a') as file_make_ex:
                file_make_ex.write(send.text + '\n')
            bot.register_next_step_handler(nstep, condition)
    except selenium.common.exceptions.WebDriverException:
        bot.delete_message(message.chat.id, message.message_id + 1)
        bot.send_message(message.chat.id, 'Попробуйте еще раз!')
        ex_start(message)


def condition(message):
    if message.text == 'Закончить и сохранить':
        bot.send_message(message.from_user.id, 'Перевод сохранен:')
        send_translate(message)
        with open('EnglishText/make_ex.txt', 'w'):
            pass
    elif message.text == 'Продолжить':
        ex_start(message)
    else:
        tupiez = bot.send_message(message.from_user.id, 'Выберете действия из клавиатуры ниже!',
                                  reply_markup=kb.keyboard_save)
        bot.register_next_step_handler(tupiez, condition)


def send_translate(message):
    with open('EnglishText/make_ex.txt', 'rt') as send_trans:
        bot.send_message(message.from_user.id, (send_trans.read()))


@bot.message_handler(commands=['list'])
def keyboard1_list(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Выберите нужную информацию:', reply_markup=kb.keyboard_menu)


@bot.message_handler(commands=['delete'])
def delete_message(message):
    i = 0
    try:
        try:
            while i < 2:
                bot.delete_message(message.chat.id, message.message_id - i)
                i = i + 1
        except telebot.apihelper.ApiException:
            i = i + 2
            bot.delete_message(message.chat.id, message.message_id - i)
    except telebot.apihelper.ApiException:
        bot.send_message(message.chat.id, 'Слишком частое использование delete\n'
                                          'Введите /clear для полной отчистки.')


@bot.message_handler(commands=['clear'])
def clear_chat(message):
    m = 0
    for msg in range(0, 200):
        try:
            bot.delete_message(message.chat.id, message.message_id - msg)
        except telebot.apihelper.ApiException:
            m = m + 1
    print(m)


def clear_list(message):
    m = 0
    for msg in range(0, 21):
        try:
            bot.delete_message(message.chat.id, message.message_id - msg)
        except telebot.apihelper.ApiException:
            m = m + 1
    print(m)


@bot.message_handler(commands=['print'])
def print_message(message):
    print(message.message_id)
    print(message.text)
    print(message.chat.id)
    print(message.from_user.id)
    print(message)
    bot.send_message(message.from_user.id, message.message_id)
    bot.send_message(message.from_user.id, message.text)
    bot.send_message(message.from_user.id, message.chat.id)
    bot.send_message(message.from_user.id, message.from_user.id)
    bot.send_message(message.from_user.id, message)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Очиcтить':
        clear_list(message)
        bot.send_message(message.from_user.id, 'Выберите нужную тему:', reply_markup=kb.keyboard_menu)
    else:
        bot.send_message(message.chat.id, 'К сожалению, тут нет смысла что-то писать, '
                                          'только команды, введите /help, чтобы посмотреть список')


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.send_message(message.chat.id, 'К сожалению, тут нет смысла отправлять стикер, '
                                      'только команды, введите /help, чтобы посмотреть список')


@bot.message_handler(content_types=['photo', 'document', 'audio', 'video', 'contact', 'location'])
def send_photo(message):
    print(message)
    bot.send_message(message.chat.id, 'К сожалению, тут нет смысла отправлять файлы, '
                                      'только команды, введите /help, чтобы посмотреть список')


bot.polling(none_stop=True)
