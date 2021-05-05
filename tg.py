import telebot
import random
import requests

bot=telebot.TeleBot('1756508816:AAHk_prvWoVNkNW7-0GHDDw0CIyvyRk2dXo')
@bot.message_handler(commands=['chance'])
def handle_start(message):
    print(message.text)
    msg='шанс того, что'
    msg+=message.text.replace('/chance','')
    msg+=' равен '+str(random.randint(0,100))
    bot.send_message(message.chat.id,msg)

@bot.message_handler(commands=['lyrics'])
def handle_start(message):

    url = "https://genius.p.rapidapi.com"

    querystring = {"q":message.text.replace('/lyrics','')}

    headers = {
        'x-rapidapi-key': "b749dd581bmshaad3442a3b1153bp15a97ajsn12dd06f55432",
        'x-rapidapi-host': "genius.p.rapidapi.com"
        }

    response = requests.request("GET", url+"/search", headers=headers, params=querystring)
    print(response.json()['response']['hits'][0]['result']['id'])
    txt = requests.get("https://genius.com/songs/"+str(response.json()['response']['hits'][0]['result']['id']), headers=headers)
    response = requests.get("https://www.youtube.com/results?search_query="+message.text.replace('/lyrics','').replace(' ','+'))
    video = response.text.split('"watchEndpoint":{"videoId":"')[1].split('"')[0]

    bot.send_message(message.chat.id,txt.text.split("<p>")[1].split("</p>")[0].replace("<br>",'')+'\nhttps://www.youtube.com/watch?v='+video)
bot.polling()