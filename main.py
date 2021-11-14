from re import S, match, split
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
    w = data['weather'][0]['description'] 
    if w == 'clear sky':
       w = "Небо безхмарне"
    elif w == "overcast clouds":
      w = "Похмуро"
    elif w == "mist":
      w = "Туман"
    elif w == "fog":
      w = "Туман"
    elif w == "scattered clouds":
      w = "Розсіяні хмари"
    elif w == "broken clouds":
      w = "Рвані хмари"
    elif w == "few clouds":
      w = "Дрібні хмари"
    elif w == "light snow":
      w = "Легкий сніг"
    elif w == "light rain":
      w = "Легкий дощ"
    elif w == "moderate rain":
      w = "Помірний дощ"
    elif w == "rain":
      w = "Дощ"
    h = data['main']['humidity'] 
    t =  data['main']['temp'] - 273
    f_t =  data['main']['feels_like'] - 273
    p =  data['main']['pressure'] 
    wind =  data['wind']['speed'] 

    www =str(w)+"\nТемпература "+str(int(t))+"°C \nВідчувається як "+str(int(t))+"°C \nВологість: "+str(h)+"%\nТиск: "+str(p)+"\nШвилкість вітру "+str(wind)+"м/с"
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