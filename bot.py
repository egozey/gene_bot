import telebot
import markups as m
import parser
TOKEN = ''
task = []
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    chat_id = message.chat.id
    if message.text == "/start":
        msg = bot.send_message(chat_id ,"Введите мутацию для поиска")
        bot.register_next_step_handler(msg, askSource)
    elif message.text == "/help":
        bot.send_message(chat_id, "не тупим", reply_markup=m.start_markup)
    else:
        bot.send_message(chat_id, "Я тебя не понимаю. Напиши /help.")

def askSource(message):

    task.append(message.text)

    chat_id = message.chat.id
    msg =bot.send_message(chat_id ,"Где искать", reply_markup=m.source_markup)

    bot.register_next_step_handler(msg, startPars)

def startPars(message):
    chat_id = message.chat.id
    task.append(message.text)
    print(task)

    bot.send_message(chat_id ,parser.pars(task[1],task[0]), reply_markup=m.start_markup)
    task.clear()






bot.polling(none_stop=True, interval=0)
