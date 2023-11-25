from django.core.management.base import BaseCommand

import telebot
from shop.models import Product

bot = telebot.TeleBot("6831587770:AAFjX33BYGXnMuHmmjHUg0_ujJQiHFzkxBk")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello World")


@bot.message_handler(commands=['apple'])
def products(message):
    products = Product.objects.all()
    for apple in products:
        bot.send_message(message.chat.id, f"product:{apple.name}, {apple.price}")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"help: /start, /apple")

@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.from_user.id, "Введите название")
    bot.register_next_step_handler(message, title_handler)

def title_handler(message):
    global title
    title = message.text

    bot.send_message(message.chat.id, "Напишите цену")
    bot.register_next_step_handler(message, price_handler)

def price_handler(message):
    global price
    price = message.text
    bot.send_message(message.chat.id, f"Отлично!")
    new_bot = Product.objects.create(name=title, price=price)

    


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
    #bot.reply_to(message, message.text)
        


class Command(BaseCommand):
   def handle(self, *args, **options):
       print("Starting bot...")
       bot.polling()
       print("Bot stopped")
   