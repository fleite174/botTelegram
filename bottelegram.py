import telebot

CHAVE_API = "6211944423:AAEGGSwfmYy1Um7zqSrJiGjmD2pD4vPKT_c"                    #chave api gerada automaticamento pelo bot

bot = telebot.TeleBot(CHAVE_API)                                                #criador do bot

@bot.message_handler(commands=["pizza"])                                       #decorator, função pizza.
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "A sua pizza saiu para entrega: tempo de espera 20 minutos")

@bot.message_handler(commands=["hamburguer"])                                   #decorator, função hamburguer.
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "O seu hamburguer saiu para entrega: tempo de espera 20 minutos")

@bot.message_handler(commands=["salada"])                                       #decorator, função salada.
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "A sua salada saiu para entrega: tempo de espera 20 minutos")

@bot.message_handler(commands=["opcao1"])                                       #decorator, função que diz quando esta informação tem que ser executada.
def opcao1(mensagem):
    texto = """"
    O que voce quer?(clique em uma opção)
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

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
    bot.reply_to(mensagem, texto)                                                #resposta padrão

bot.polling()