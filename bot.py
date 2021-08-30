import telebot
import markups as m
import parser
TOKEN = '1974316775:AAHnGEST2F6-ALoP1gGsnDgkG7HxkK_86Vc'
task = {}
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    task[chat_id] = []
    if message.text == "/start":
        msg = bot.send_message(chat_id ,"Введите мутацию для поиска")
        bot.register_next_step_handler(msg, askSource)
    elif message.text == "/help":
        bot.send_message(chat_id, "Для поиска мутации наберите на клавиатуре (или нажмите кнопку) /start", reply_markup=m.start_markup)
    else:
        bot.send_message(chat_id, "Я тебя не понимаю. Напиши /help.")

def askSource(message):
    chat_id = message.chat.id
    if message.text.lower == "c" or message.text.lower == "с" :
        msg =bot.send_message(chat_id ,"МАЛО ИНФОРМАЦИИ ДЛЯ ПОИСКА", reply_markup=m.start_markup)
        return pass
    else:
        task[chat_id].append(message.text)
        msg =bot.send_message(chat_id ,"Где искать", reply_markup=m.source_markup)

    bot.register_next_step_handler(msg, startPars)

def startPars(message):
    chat_id = message.chat.id
    task[chat_id].append(message.text)
    print(task)

    bot.send_message(chat_id ,parser.pars(task[chat_id][1],task[chat_id][0]), reply_markup=m.start_markup)
    del(task[chat_id])





bot.polling(none_stop=True, interval=0)
