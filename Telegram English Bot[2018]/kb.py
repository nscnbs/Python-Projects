from telebot.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Кнопка 'Очиcтить'
delete1 = KeyboardButton('Очиcтить')

keyboard_delete = ReplyKeyboardMarkup(True, True)
keyboard_delete.add(delete1)


# Кнопка 'Coxранить и cкинуть'
save1 = KeyboardButton('Продолжить')
save2 = KeyboardButton('Закончить и сохранить')

keyboard_save = ReplyKeyboardMarkup(True, True)
keyboard_save.add(save1, save2)

# Начальная панель
menu1 = InlineKeyboardButton('Теория', callback_data='mn1')
menu2 = InlineKeyboardButton('Упражнения', callback_data='mn2')
menu3 = InlineKeyboardButton('Переводчик Google (En-Ru)', callback_data='mn3')
menu4 = InlineKeyboardButton('Работа с упражнениями', callback_data='mn4')

keyboard_menu = InlineKeyboardMarkup(row_width=1)
keyboard_menu.add(menu1, menu2, menu3, menu4)


# Панель 'Теория'
theory1 = InlineKeyboardButton('Modal Verbs', callback_data='thr1')
theory2 = InlineKeyboardButton('Appearance and Character', callback_data='thr2')
theory3 = InlineKeyboardButton('Gerund', callback_data='thr3')
theory4 = InlineKeyboardButton('Participle', callback_data='thr4')
theory5 = InlineKeyboardButton('Future in the Past', callback_data='thr5')
theory_back = InlineKeyboardButton('↩', callback_data='thr0')

keyboard_theory = InlineKeyboardMarkup(row_width=1)
keyboard_theory.add(theory1, theory2, theory3, theory4, theory5, theory_back)


# Панель 'Упражнения'
exer1 = InlineKeyboardButton('Modal Verbs', callback_data='ex1')
exer2 = InlineKeyboardButton('Participle', callback_data='ex2')
exer3 = InlineKeyboardButton('Passive Voice', callback_data='ex3')
exer4 = InlineKeyboardButton('Gerund (20.07.19)', callback_data='ex4')
exer5 = InlineKeyboardButton('Translation', callback_data='ex5')
exer6 = InlineKeyboardButton('Texts', callback_data='ex6')
exer7 = InlineKeyboardButton('Words', callback_data='ex7')
exer8 = InlineKeyboardButton('Unknown Book', callback_data='ex8')
exer_back = InlineKeyboardButton('↩', callback_data='ex0')

keyboard_exercise = InlineKeyboardMarkup(row_width=1)
keyboard_exercise.add(exer1, exer2, exer3, exer4, exer5, exer6, exer7, exer8, exer_back)


# Панель 'Modal Verbs' в 'Теория'
modal1 = InlineKeyboardButton('Be to', callback_data='mdl1')
modal2 = InlineKeyboardButton('Can/Could', callback_data='mdl2')
modal3 = InlineKeyboardButton('May/Might', callback_data='mdl3')
modal4 = InlineKeyboardButton('Must/Have to', callback_data='mdl4')
modal5 = InlineKeyboardButton('Shall/Will', callback_data='mdl5')
modal6 = InlineKeyboardButton('Would', callback_data='mdl6')
modal7 = InlineKeyboardButton('Dare', callback_data='mdl7')
modal8 = InlineKeyboardButton('Theory Modal Verbs', callback_data='mdl8')
modal_back = InlineKeyboardButton('↩', callback_data='mdl0')

keyboard_modal = InlineKeyboardMarkup(row_width=1)
keyboard_modal.add(modal1, modal2, modal3, modal4, modal5, modal6, modal7, modal8, modal_back)

# Панель 'Appearance and Character' в 'Теория'
appear1 = InlineKeyboardButton('Appearance', callback_data='app1')
appear2 = InlineKeyboardButton('Character', callback_data='app2')
appear_back = InlineKeyboardButton('↩', callback_data='app0')

keyboard_appearance = InlineKeyboardMarkup(row_width=1)
keyboard_appearance.add(appear1, appear2, appear_back)


# Панель 'Modal Verbs' в 'Упражнения'
modal_ex1 = InlineKeyboardButton('Be to/Have to', callback_data='mod1')
modal_ex2 = InlineKeyboardButton('Can/May/Must', callback_data='mod2')
modal_ex3 = InlineKeyboardButton('Modal (04.07.19)', callback_data='mod3')
modal_ex4 = InlineKeyboardButton('Must (09.04.20)', callback_data='mod4')
modal_ex5 = InlineKeyboardButton('Shall/Will', callback_data='mod5')
modal_ex6 = InlineKeyboardButton('Will/Would (09.05.20)', callback_data='mod6')
modal_ex7 = InlineKeyboardButton('Dare (09.05.20)', callback_data='mod7')
modal_exback = InlineKeyboardButton('↩', callback_data='mod0')

keyboard_modal_ex = InlineKeyboardMarkup(row_width=1)
keyboard_modal_ex.add(modal_ex1, modal_ex2, modal_ex3, modal_ex4, modal_ex5, modal_ex6, modal_ex7, modal_exback)

# Панель 'Be to/Have to' в Modal Verbs в 'Упражнения'
beto_ex1 = InlineKeyboardButton('Be to (08.07.19)', callback_data='bet1')
beto_ex2 = InlineKeyboardButton('Be to (17.04.20)', callback_data='bet2')
beto_ex3 = InlineKeyboardButton('Be to/Have to (11.07.19)', callback_data='bet3')
beto_ex4 = InlineKeyboardButton('Be to/Have to (16.04.20)', callback_data='bet4')
beto_ex5 = InlineKeyboardButton('Be to/Have to (17.04.20)', callback_data='bet5')
beto_exback = InlineKeyboardButton('↩', callback_data='bet0')

keyboard_beto_ex = InlineKeyboardMarkup(row_width=1)
keyboard_beto_ex.add(beto_ex1, beto_ex2, beto_ex3, beto_ex4, beto_ex5, beto_exback)

# Панель 'Can/May/Must' в Modal Verbs в 'Упражнения'
can_ex1 = InlineKeyboardButton('Can (27.03.20)', callback_data='can1')
can_ex2 = InlineKeyboardButton('Can/May (02.04.20)', callback_data='can2')
can_ex3 = InlineKeyboardButton('Can/May (02.04.20) v.2', callback_data='can3')
can_ex4 = InlineKeyboardButton('Can/May/Must (09.04.20)', callback_data='can4')
can_exback = InlineKeyboardButton('↩', callback_data='can0')

keyboard_can_ex = InlineKeyboardMarkup(row_width=1)
keyboard_can_ex.add(can_ex1, can_ex2, can_ex3, can_ex4, can_exback)

# Панель 'Shall/Will' в Modal Verbs в 'Упражнения'
shall_ex1 = InlineKeyboardButton('Shall/Will (23.04.20)', callback_data='shall1')
shall_ex2 = InlineKeyboardButton('Shall/Will (30.04.20)', callback_data='shall2')
shall_exback = InlineKeyboardButton('↩', callback_data='shall0')

keyboard_shall_ex = InlineKeyboardMarkup(row_width=1)
keyboard_shall_ex.add(shall_ex1, shall_ex2, shall_exback)

# Панель 'Participle' в 'Упражнения'
participle_ex1 = InlineKeyboardButton('Participle (04.11.19)', callback_data='part1')
participle_ex2 = InlineKeyboardButton('Participle (04.11.19) v.2', callback_data='part2')
participle_ex3 = InlineKeyboardButton('Participle (07.11.19)', callback_data='part3')
participle_ex4 = InlineKeyboardButton('Participle (13.11.19)', callback_data='part4')
participle_ex5 = InlineKeyboardButton('Participle (01.12.19)', callback_data='part5')
participle_exback = InlineKeyboardButton('↩', callback_data='part0')

keyboard_participle_ex = InlineKeyboardMarkup(row_width=1)
keyboard_participle_ex.add(participle_ex1, participle_ex2, participle_ex3, participle_ex4, participle_ex5, participle_exback)


# Панель 'Passive Voice' в 'Упражнения'
passive_ex1 = InlineKeyboardButton('Passive Voice (01.11.18)', callback_data='pass1')
passive_ex2 = InlineKeyboardButton('Passive Voice (18.02.19)', callback_data='pass2')
passive_exback = InlineKeyboardButton('↩', callback_data='pass0')

keyboard_passive_ex = InlineKeyboardMarkup(row_width=1)
keyboard_passive_ex.add(passive_ex1, passive_ex2, passive_exback)

# Панель 'Translation' в 'Упражнения'
translate_ex1 = InlineKeyboardButton('Translation (26.03.18)', callback_data='trans1')
translate_ex2 = InlineKeyboardButton('Translation (05.01.19)', callback_data='trans2')
translate_ex3 = InlineKeyboardButton('Translation (11.02.19)', callback_data='trans3')
translate_ex4 = InlineKeyboardButton('Translation (24.07.19)', callback_data='trans4')
translate_ex5 = InlineKeyboardButton('Translation (18.11.19)', callback_data='trans5')
translate_ex6 = InlineKeyboardButton('Translation (02.12.19)', callback_data='trans6')
translate_ex7 = InlineKeyboardButton('Translation (09.12.19)', callback_data='trans7')
translate_exback = InlineKeyboardButton('↩', callback_data='trans0')

keyboard_translate_ex = InlineKeyboardMarkup(row_width=1)
keyboard_translate_ex.add(translate_ex1, translate_ex2, translate_ex3, translate_ex4, translate_ex5, translate_ex6, translate_ex7, translate_exback)


# Панель 'Texts' в 'Упражнения'
text_ex1 = InlineKeyboardButton('Chocolate - Food of the Gods (17.01.19)', callback_data='text1')
text_ex2 = InlineKeyboardButton('Cosmic Black Holes (21.01.19)', callback_data='text2')
text_ex3 = InlineKeyboardButton('Model Teacher (25.02.19)', callback_data='text3')
text_ex4 = InlineKeyboardButton('Text (18.03.19)', callback_data='text4')
text_ex5 = InlineKeyboardButton('A Lilac Bush (08.04.19)', callback_data='text5')
text_ex6 = InlineKeyboardButton('Meals (16.05.19)', callback_data='text6')
text_ex7 = InlineKeyboardButton('Have You Ever Been to Peru (26.03.20)', callback_data='text7')
text_ex8 = InlineKeyboardButton('Prairie Dog with Sweet Tooth Found on Farm (26.03.20)', callback_data='text8')
text_exback = InlineKeyboardButton('↩', callback_data='text0')

keyboard_text_ex = InlineKeyboardMarkup(row_width=1)
keyboard_text_ex.add(text_ex1, text_ex2, text_ex3, text_ex4, text_ex5, text_ex6, text_ex7, text_ex8, text_exback)


# Панель 'Words' в 'Упражнения'
word_ex1 = InlineKeyboardButton('Phrases (27.03.19)', callback_data='word1')
word_ex2 = InlineKeyboardButton('Sentences (14.03.19)', callback_data='word2')
word_ex3 = InlineKeyboardButton('Sentences (08.04.19)', callback_data='word3')
word_ex4 = InlineKeyboardButton('Discussing Arrangements for a Party (08.04.19)', callback_data='word4')
word_ex5 = InlineKeyboardButton('Put Word (21.03.20)', callback_data='word5')
word_ex6 = InlineKeyboardButton('Put Word (22.03.20)', callback_data='word6')
word_exback = InlineKeyboardButton('↩', callback_data='word0')

keyboard_word_ex = InlineKeyboardMarkup(row_width=1)
keyboard_word_ex.add(word_ex1, word_ex2, word_ex3, word_ex4, word_exback)

# Панель 'Unknown Book' в 'Упражнения'
unkbook_ex1 = InlineKeyboardButton('ex.1,2,3 p.262 (31.07.18)', callback_data='unk1')
unkbook_ex2 = InlineKeyboardButton('ex.18,19 p.55 (22.10.18)', callback_data='unk2')
unkbook_ex3 = InlineKeyboardButton('ex.5,6 p.157 (05.11.18)', callback_data='unk3')
unkbook_ex4 = InlineKeyboardButton('ex.5,6 p.188 (05.11.18)', callback_data='unk4')
unkbook_ex5 = InlineKeyboardButton('ex.10,14 p.192 (18.11.18)', callback_data='unk5')
unkbook_ex6 = InlineKeyboardButton('ex.23 p.54 (27.12.18)', callback_data='unk6')
unkbook_ex7 = InlineKeyboardButton('ex.27,28 p.164 (27.12.18)', callback_data='unk7')
unkbook_ex8 = InlineKeyboardButton('ex.9 p.153 (16.05.20)', callback_data='unk8')
unkbook_exback = InlineKeyboardButton('↩', callback_data='unk0')

keyboard_unkbook_ex = InlineKeyboardMarkup(row_width=1)
keyboard_unkbook_ex.add(unkbook_ex1, unkbook_ex2, unkbook_ex3, unkbook_ex4, unkbook_ex5, unkbook_ex6, unkbook_ex7, unkbook_ex8, unkbook_exback)


# Панель 'Работа с упражнениями'
makeex1 = InlineKeyboardButton('Создать упражнение(Перевод с En-Ru)', callback_data='mex1')
makeex2 = InlineKeyboardButton('Создать упражнение(Перевод с Ru-En)', callback_data='mex2')
makeex_back = InlineKeyboardButton('↩', callback_data='mex0')

keyboard_make_ex = InlineKeyboardMarkup(row_width=1)
keyboard_make_ex.add(makeex1, makeex2, makeex_back)

