from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('APC')
source_markup_btn2 = types.KeyboardButton('MLH1')
source_markup_btn3 = types.KeyboardButton('MLH3')
source_markup_btn4 = types.KeyboardButton('MSH2')
source_markup_btn5 = types.KeyboardButton('MSH6')
source_markup_btn6 = types.KeyboardButton('MUTYH')
source_markup.add(source_markup_btn1, source_markup_btn2,source_markup_btn3,source_markup_btn4,source_markup_btn5,source_markup_btn6)


