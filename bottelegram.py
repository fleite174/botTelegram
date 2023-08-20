import telebot

CHAVE_API = "6211944423:AAEGGSwfmYy1Um7zqSrJiGjmD2pD4vPKT_c"                    #chave api gerada automaticamento pelo bot

bot = telebot.TeleBot(CHAVE_API)                                                #criador do bot

@bot.message_handler(commands=["opcao1"])                                       #decorator, função que diz quando esta informação tem que ser executada.
def opcao1(mensagem):
    pass

@bot.message_handler(commands=["opcao2"])                                       #decorator, função que diz quando esta informação tem que ser executada.
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para etc@etc.com")
    

@bot.message_handler(commands=["opcao3"])                                       #decorator, função que diz quando esta informação tem que ser executada.
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! Dezin manda uma abraço de dentro da McLaren 720S GT3")



def verificar(mensagem):                                                        #mensagem padrão para primeiro contato com o bot.  
    return True

@bot.message_handler()                                                          #decorator, função que diz quando esta informação tem que ser executada.
def responder(mensagem):
    texto = """ 
    Escolha uma opção para continuar(Clique no item):
        /opcao1 Fazer um pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mandar um abraço para o Dezin
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)           #resposta padrão


bot.polling()