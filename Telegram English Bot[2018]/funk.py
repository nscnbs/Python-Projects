import telebot
import cfg
import kb
import file

bot = telebot.TeleBot(cfg.TOKEN)


# MODAL VERBS PHOTO
def photo_be_to(callback_query):
    bot.send_photo(callback_query.from_user.id, file.beto1, reply_markup=kb.keyboard_delete)


def photo_can(callback_query):
    for i in range(0, len(file.can)):
        bot.send_photo(callback_query.from_user.id, file.can[i], reply_markup=kb.keyboard_delete)


def photo_may(callback_query):
    for i in range(0, len(file.may)):
        bot.send_photo(callback_query.from_user.id, file.may[i], reply_markup=kb.keyboard_delete)


def photo_must(callback_query):
    for i in range(0, len(file.must)):
        bot.send_photo(callback_query.from_user.id, file.must[i], reply_markup=kb.keyboard_delete)


def photo_shall(callback_query):
    for i in range(0, len(file.shall)):
        bot.send_photo(callback_query.from_user.id, file.shall[i], reply_markup=kb.keyboard_delete)


def photo_would(callback_query):
    bot.send_photo(callback_query.from_user.id, file.would1, reply_markup=kb.keyboard_delete)


def photo_dare(callback_query):
    bot.send_photo(callback_query.from_user.id, file.dare1, reply_markup=kb.keyboard_delete)


def modal_theory(callback_query):
    with open('EnglishText/TheoryModal.txt', 'rt') as modal1:
        bot.send_message(callback_query.from_user.id, (modal1.read()))


# APPEREANCE AND CHARACTER PHOTO
def photo_appearance(callback_query):
    for i in range(0, len(file.app)):
        bot.send_photo(callback_query.from_user.id, file.app[i], reply_markup=kb.keyboard_delete)


def photo_character(callback_query):
    for i in range(0, len(file.chcr)):
        bot.send_photo(callback_query.from_user.id, file.chcr[i], reply_markup=kb.keyboard_delete)


# Gerund
def photo_gerund(callback_query):
    for i in range(0, len(file.ger)):
        bot.send_photo(callback_query.from_user.id, file.ger[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/Gerund Words.txt', 'rt') as ex_modal1:
        bot.send_message(callback_query.from_user.id, (ex_modal1.read()))


# Participle
def photo_participle(callback_query):
    for i in range(0, len(file.par)):
        bot.send_photo(callback_query.from_user.id, file.par[i], reply_markup=kb.keyboard_delete)


# Future in the Past
def photo_future(callback_query):
    bot.send_photo(callback_query.from_user.id, file.future1, reply_markup=kb.keyboard_delete)


# MODAL VERBS exercise

# Be to ex
def exercise_be_to1(callback_query):
    for i in range(0, len(file.beto_ex)):
        bot.send_photo(callback_query.from_user.id, file.beto_ex[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/be_to.08.07.19.txt', 'rt') as ex_be_to1:
        bot.send_message(callback_query.from_user.id, (ex_be_to1.read()))


def exercise_be_to2(callback_query):
    bot.send_photo(callback_query.from_user.id, file.beto_ex3, reply_markup=kb.keyboard_delete)
    with open('EnglishText/be_to.17.04.20.txt', 'rt') as ex_be_to2:
        bot.send_message(callback_query.from_user.id, (ex_be_to2.read()))


def exercise_be_to3(callback_query):
    bot.send_photo(callback_query.from_user.id, file.beto_ex4, reply_markup=kb.keyboard_delete)
    with open('EnglishText/be_to.have_to.11.07.19.txt', 'rt') as ex_be_to3:
        bot.send_message(callback_query.from_user.id, (ex_be_to3.read()))


def exercise_be_to4(callback_query):
    bot.send_photo(callback_query.from_user.id, file.beto_ex5, reply_markup=kb.keyboard_delete)
    with open('EnglishText/be_to.have_to.16.04.20.txt', 'rt') as ex_be_to4:
        bot.send_message(callback_query.from_user.id, (ex_be_to4.read()))


def exercise_be_to5(callback_query):
    bot.send_photo(callback_query.from_user.id, file.beto_ex6, reply_markup=kb.keyboard_delete)
    with open('EnglishText/be_to.have_to.17.04.20.txt', 'rt') as ex_be_to5:
        bot.send_message(callback_query.from_user.id, (ex_be_to5.read()))


# Can ex
def exercise_can1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.can_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/can.27.03.20.txt', 'rt') as ex_can1:
        bot.send_message(callback_query.from_user.id, (ex_can1.read()))


def exercise_can2(callback_query):
    bot.send_photo(callback_query.from_user.id, file.can_ex2, reply_markup=kb.keyboard_delete)
    with open('EnglishText/can.may.02.04.20.txt', 'rt') as ex_can2:
        bot.send_message(callback_query.from_user.id, (ex_can2.read()))


def exercise_can3(callback_query):
    bot.send_photo(callback_query.from_user.id, file.can_ex3, reply_markup=kb.keyboard_delete)
    with open('EnglishText/can.may.02.04.20.v2.txt', 'rt') as ex_can3:
        bot.send_message(callback_query.from_user.id, (ex_can3.read()))


def exercise_can4(callback_query):
    bot.send_photo(callback_query.from_user.id, file.can_ex4, reply_markup=kb.keyboard_delete)
    with open('EnglishText/can.may.must.09.04.20.txt', 'rt') as ex_can4:
        bot.send_message(callback_query.from_user.id, (ex_can4.read()))


# Dare
def exercise_dare1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.dare_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/dare.09.05.20.txt', 'rt') as ex_dare1:
        bot.send_message(callback_query.from_user.id, (ex_dare1.read()))


# Shall
def exercise_shall1(callback_query):
    for i in range(0, len(file.shall_ex_1)):
        bot.send_photo(callback_query.from_user.id, file.shall_ex_1[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/shall.will.23.04.20.txt', 'rt') as ex_shall1:
        bot.send_message(callback_query.from_user.id, (ex_shall1.read()))


def exercise_shall2(callback_query):
    for i in range(0, len(file.shall_ex_2)):
        bot.send_photo(callback_query.from_user.id, file.shall_ex_2[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/shall.will.30.04.20.txt', 'rt') as ex_shall2:
        bot.send_message(callback_query.from_user.id, (ex_shall2.read()))


# Modal
def exercise_modal1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.modal_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/modal.04.07.19.txt', 'rt') as ex_modal1:
        bot.send_message(callback_query.from_user.id, (ex_modal1.read()))


# Must
def exercise_must1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.must_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/must.09.04.20.txt', 'rt') as ex_must1:
        bot.send_message(callback_query.from_user.id, (ex_must1.read()))


# Will
def exercise_will1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.will_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/will.would.09.05.20.txt', 'rt') as ex_will1:
        bot.send_message(callback_query.from_user.id, (ex_will1.read()))


# Participle
def exercise_participle1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.participle_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/participle.04.11.19.txt', 'rt') as ex_participle1:
        bot.send_message(callback_query.from_user.id, (ex_participle1.read()))


def exercise_participle2(callback_query):
    bot.send_photo(callback_query.from_user.id, file.participle_ex2, reply_markup=kb.keyboard_delete)
    with open('EnglishText/participle.04.11.19.v2.txt', 'rt') as ex_participle2:
        bot.send_message(callback_query.from_user.id, (ex_participle2.read()))


def exercise_participle3(callback_query):
    bot.send_photo(callback_query.from_user.id, file.participle_ex3, reply_markup=kb.keyboard_delete)
    with open('EnglishText/participle.07.11.19.txt', 'rt') as ex_participle3:
        bot.send_message(callback_query.from_user.id, (ex_participle3.read()))


def exercise_participle4(callback_query):
    with open('EnglishText/participle.13.11.19.txt', 'rt') as ex_participle4:
        bot.send_message(callback_query.from_user.id, (ex_participle4.read()))


def exercise_participle5(callback_query):
    bot.send_photo(callback_query.from_user.id, file.participle_ex4, reply_markup=kb.keyboard_delete)
    with open('EnglishText/participle.01.12.19.txt', 'rt') as ex_participle5:
        bot.send_message(callback_query.from_user.id, (ex_participle5.read()))


# Passive
def exercise_passive1(callback_query):
    with open('EnglishText/passive.01.11.18.txt', 'rt') as ex_passive1:
        bot.send_message(callback_query.from_user.id, (ex_passive1.read()))


def exercise_passive2(callback_query):
    bot.send_photo(callback_query.from_user.id, file.passive_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/passive.18.02.19.txt', 'rt') as ex_passive2:
        bot.send_message(callback_query.from_user.id, (ex_passive2.read()))


# Gerund
def exercise_gerund1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.gerund_ex1, reply_markup=kb.keyboard_delete)
    with open('EnglishText/gerund.20.07.19.txt', 'rt') as ex_ger1:
        bot.send_message(callback_query.from_user.id, (ex_ger1.read()))


# Translate
def exercise_translate1(callback_query):
    with open('EnglishText/ex_translate.26.03.18.txt', 'rt') as ex_trans1:
        bot.send_message(callback_query.from_user.id, (ex_trans1.read()))


def exercise_translate2(callback_query):
    for i in range(0, len(file.translate_ex_1)):
        bot.send_photo(callback_query.from_user.id, file.translate_ex_1[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_translate.05.01.19.txt', 'rt') as ex_trans2:
        bot.send_message(callback_query.from_user.id, (ex_trans2.read()))


def exercise_translate3(callback_query):
    bot.send_photo(callback_query.from_user.id, file.translate_ex3, reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_translate.11.02.19.txt', 'rt') as ex_trans3:
        bot.send_message(callback_query.from_user.id, (ex_trans3.read()))


def exercise_translate4(callback_query):
    bot.send_photo(callback_query.from_user.id, file.translate_ex4, reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_translate.24.07.19.txt', 'rt') as ex_trans4:
        bot.send_message(callback_query.from_user.id, (ex_trans4.read()))


def exercise_translate5(callback_query):
    bot.send_photo(callback_query.from_user.id, file.translate_ex5, reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_translate.18.11.19.txt', 'rt') as ex_trans5:
        bot.send_message(callback_query.from_user.id, (ex_trans5.read()))


def exercise_translate6(callback_query):
    bot.send_photo(callback_query.from_user.id, file.translate_ex6, reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_translate.02.12.19.txt', 'rt') as ex_trans6:
        bot.send_message(callback_query.from_user.id, (ex_trans6.read()))


def exercise_translate7(callback_query):
    bot.send_photo(callback_query.from_user.id, file.translate_ex7, reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_translate.09.12.19.txt', 'rt') as ex_trans7:
        bot.send_message(callback_query.from_user.id, (ex_trans7.read()))


# Text
def exercise_text1(callback_query):
    for i in range(0, len(file.text_ex_1)):
        bot.send_photo(callback_query.from_user.id, file.text_ex_1[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.17.01.19.txt', 'rt') as ex_text1:
        bot.send_message(callback_query.from_user.id, (ex_text1.read()))


def exercise_text2(callback_query):
    for i in range(0, len(file.text_ex_2)):
        bot.send_photo(callback_query.from_user.id, file.text_ex_2[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.21.01.19.txt', 'rt') as ex_text2:
        bot.send_message(callback_query.from_user.id, (ex_text2.read()))


def exercise_text3(callback_query):
    bot.send_photo(callback_query.from_user.id, file.text_ex8, reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.25.02.19.txt', 'rt') as ex_text3:
        bot.send_message(callback_query.from_user.id, (ex_text3.read()))


def exercise_text4(callback_query):
    bot.send_photo(callback_query.from_user.id, file.text_ex9, reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.18.03.19.txt', 'rt') as ex_text4:
        bot.send_message(callback_query.from_user.id, (ex_text4.read()))


def exercise_text5(callback_query):
    for i in range(0, len(file.text_ex_3)):
        bot.send_photo(callback_query.from_user.id, file.text_ex_3[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.08.04.19.txt', 'rt') as ex_text5:
        bot.send_message(callback_query.from_user.id, (ex_text5.read()))


def exercise_text6(callback_query):
    for i in range(0, len(file.text_ex_4)):
        bot.send_photo(callback_query.from_user.id, file.text_ex_4[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.16.05.19.txt', 'rt') as ex_text6:
        bot.send_message(callback_query.from_user.id, (ex_text6.read()))
    with open('EnglishText/text.poland.16.05.19.txt', 'rt') as ex_text7:
        bot.send_message(callback_query.from_user.id, (ex_text7.read()))


def exercise_text7(callback_query):
    bot.send_photo(callback_query.from_user.id, file.text_ex14, reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.26.03.20.txt', 'rt') as ex_text8:
        bot.send_message(callback_query.from_user.id, (ex_text8.read()))


def exercise_text8(callback_query):
    bot.send_photo(callback_query.from_user.id, file.text_ex15, reply_markup=kb.keyboard_delete)
    with open('EnglishText/text.v2.26.03.20.txt', 'rt') as ex_text9:
        bot.send_message(callback_query.from_user.id, (ex_text9.read()))


# Word
# 27.03.18
def exercise_word1(callback_query):
    bot.send_photo(callback_query.from_user.id, file.word_ex1, reply_markup=kb.keyboard_delete)


def exercise_word2(callback_query):
    with open('EnglishText/words.sentences.14.03.19.txt', 'rt') as ex_word2:
        bot.send_message(callback_query.from_user.id, (ex_word2.read()))


def exercise_word3(callback_query):
    for i in range(0, len(file.word_ex_2)):
        bot.send_photo(callback_query.from_user.id, file.word_ex_2[i], reply_markup=kb.keyboard_delete)
    with open('EnglishText/words.sentences.08.04.19.txt', 'rt') as ex_word3:
        bot.send_message(callback_query.from_user.id, (ex_word3.read()))


def exercise_word4(callback_query):
    bot.send_photo(callback_query.from_user.id, file.word_ex7, reply_markup=kb.keyboard_delete)
    with open('EnglishText/party.dialog.08.04.19.txt', 'rt') as ex_word4:
        bot.send_message(callback_query.from_user.id, (ex_word4.read()))


def exercise_word5(callback_query):
    bot.send_photo(callback_query.from_user.id, file.word_ex8, reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_put_word.21.03.20.txt', 'rt') as ex_word5:
        bot.send_message(callback_query.from_user.id, (ex_word5.read()))


def exercise_word6(callback_query):
    bot.send_photo(callback_query.from_user.id, file.word_ex9, reply_markup=kb.keyboard_delete)
    with open('EnglishText/ex_put_word.22.03.20.txt', 'rt') as ex_word6:
        bot.send_message(callback_query.from_user.id, (ex_word6.read()))


# Unknown book
def exercise_unkbook1(callback_query):
    with open('EnglishText/Unknown Book/ex.1,2,3 p.262.31.07.18.txt', 'rt') as ex_unkb1:
        bot.send_message(callback_query.from_user.id, (ex_unkb1.read()))


def exercise_unkbook2(callback_query):
    with open('EnglishText/Unknown Book/ex.18,19 p.55.22.10.18.txt', 'rt') as ex_unkb2:
        bot.send_message(callback_query.from_user.id, (ex_unkb2.read()))


def exercise_unkbook3(callback_query):
    with open('EnglishText/Unknown Book/ex.5,6p.157.05.11.18.txt', 'rt') as ex_unkb3:
        bot.send_message(callback_query.from_user.id, (ex_unkb3.read()))


def exercise_unkbook4(callback_query):
    with open('EnglishText/Unknown Book/ex.5,6p.188.05.11.18.txt', 'rt') as ex_unkb4:
        bot.send_message(callback_query.from_user.id, (ex_unkb4.read()))


def exercise_unkbook5(callback_query):
    with open('EnglishText/Unknown Book/ex.10,14 p.192.18.11.18.txt', 'rt') as ex_unkb5:
        bot.send_message(callback_query.from_user.id, (ex_unkb5.read()))


def exercise_unkbook6(callback_query):
    with open('EnglishText/Unknown Book/ex. 23 p.54.27.12.18.txt', 'rt') as ex_unkb6:
        bot.send_message(callback_query.from_user.id, (ex_unkb6.read()))


def exercise_unkbook7(callback_query):
    with open('EnglishText/Unknown Book/ex. 27, 28 p.164.27.12.18.txt', 'rt') as ex_unkb7:
        bot.send_message(callback_query.from_user.id, (ex_unkb7.read()))


def exercise_unkbook8(callback_query):
    with open('EnglishText/Unknown Book/ex.9 p.153.16.05.20.txt', 'rt') as ex_unkb8:
        bot.send_message(callback_query.from_user.id, (ex_unkb8.read()))
