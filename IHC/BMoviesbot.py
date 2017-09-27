import telepot

#atribuindo token ao Bot
bot = telepot.Bot("444778927:AAEIM7sIL9PM5hfl-VtqQAQaqj2-BwujQ68")


while(True):
    pass

count = 0
updates = bot.getUpdates(-1)

chatId = updates[0]['message']['chat']['id']
username = updates[0]['message']['chat']['username']
mensagem = updates[0]['message']['text']

if(mensagem == "/start"):
    bot.sendMessage(chatId, 'Olá %s'%username)
