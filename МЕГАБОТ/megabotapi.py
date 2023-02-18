import telebot
from telebot import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
token='5894468261:AAEtj7hqzV049eww6XhgNx9pbSeCZ2Pp_jU'
bot=telebot.TeleBot(token)
button_hi = KeyboardButton('Привет! 👋')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помошник!, напиши /help")

@bot.message_handler(commands=['help'])
def process_start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("узнать расписание")
    btn2 = types.KeyboardButton("записаться на мегакурс")
    btn3=types.KeyboardButton("наш сайт")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id,"Привет",reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text=="узнать расписание":
        bot.send_message(message.chat.id,"завтра хавать")
        doc=open('schedule.docx','rb')
        bot.send_document(chat_id=message.chat.id,document=doc)
    elif message.text=="записаться на мегакурс":
        bot.send_message(message.chat.id, "пока нет")
    elif message.text=="наш сайт":
        sitekb=types.InlineKeyboardMarkup()
        st_kb=types.InlineKeyboardButton(text='мегасайт',url='http://olympia.ga')
        sitekb.add(st_kb)
        bot.send_message(message.chat.id,'наш сайт',reply_markup=sitekb)

bot.infinity_polling()
