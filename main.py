from re import split
import telebot
from telebot.types import Message
import time
import requests
token = '2143900806:AAF8dm4zpODLuKSohzlyELloipHfDaJkI1c'

def getWeather(city):
  try:
    city = str(city)
    city.title()
    res = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0efdd3ecd2a008f997522da842192aa0")
    data = res.json()
    a = data['weather'][0]['description'] 
    b =  data['main']['temp'] - 273
    www = "Weater is "+str(a)+"\nTemperatre: "+str(int(b))+"°C"
    return www
  except Exception as e:
    return("Населений пункт вказано невірно"+ u'😢', e)


bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привіт🖐")
  time.sleep(1)
  bot.send_message(message.chat.id,"Подивитись погоду /weather")
@bot.message_handler(commands=['end'])
def start_message(message):
  bot.send_message(message.chat.id,"")

@bot.message_handler(commands=['weather'])
def start_message(message):
  bot.send_message(message.chat.id,"Введи свій насалений пункт (англійською)")
time.sleep(2)
@bot.message_handler()
def start_message(message):
    bot.send_message(message.chat.id,getWeather(message.text))
bot.polling(non_stop=True)