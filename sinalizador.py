import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup 
from telegram.ext import CallbackQueryHandler
from telegram.ext.updater import Updater # Conter a chave da api vinda do botfather
from telegram.update import Update # Isso será invocado toda vez que um bot receber uma atualização
from telegram.ext.callbackcontext import CallbackContext # Não usaremos sua funcionalidade diretamente em nosso código, mas quando adicionarmos o dispatcher, será necessário (e funcionará internamente)
from telegram.ext.commandhandler import CommandHandler #Esta classe Handler é usada para lidar com qualquer comando enviado pelo usuário ao bot, um comando sempre começa com “/” ou seja, “/start”,”/help” etc.
from telegram.ext.messagehandler import MessageHandler #Esta classe Handler é usada para lidar com qualquer mensagem normal enviada pelo usuário ao bot
from telegram.ext.filters import Filters # Isso filtrará texto normal, comandos, imagens, etc. de uma mensagem enviada.

from dados import selecionaTodosClientes, SelecionaTodosSinais
from src.estrategia import encontrarEstrategia

print('Telegram bot inicialiado')

updater = Updater("5350481212:AAEpiE5l-qYkEommV2AvQ5oBUS1-qt9jqSQ", use_context=True)

estrategiasEnum = ['vermelho', 'preto', 'impar', 'par', 'alto', 'baixo', 'duzia-01', 'duzia-02', 'duzia-03', 'coluna-01', 'coluna-02', 'coluna-03']
estrategias = [0,0,0,0,0,0,0,0,0,0,0]

# 0 - vermelho & preto
sinaisAnunciados = [0] 



def verificaAnalisando():
    analisando = False
    estrategia = 'Não definido'

    if estrategias[0] == 10 and sinaisAnunciados[0] == 0:
        analisando = True
        sinaisAnunciados[0] = 1

    if estrategias[1] == 10 and sinaisAnunciados[0]:
        analisando = True
        sinaisAnunciados[0] = 1

    return analisando,estrategia


def verificaSinalConfirmado():
    analisando = False
    estrategia = 'Não definido'

    if estrategias[0] == 11 and sinaisAnunciados[0] == 1:
        analisando = True
        
    return analisando,estrategia
    


while True:

    # Analisando estrategias 
    time.sleep(5)
    tipo = 'playtech'
    mesa = 'ROLETA-BRASILEIRA'
    sinais = SelecionaTodosSinais(tipo)

    print()

    
    for sinal in sinais:
        estrategias = encontrarEstrategia(sinal['value'],estrategias)

        verificacaoSinais,estrategia = verificaAnalisando() # verifica se precisa informar ao usuario que a mesa esta sendo analisada
        if verificacaoSinais == True:
            
            clientes = selecionaTodosClientes()
            for cliente in clientes:
                updater.bot.send_message(int(cliente['chat_id']), '*⏱️ Analisando mesa*\n\n* 🎰 Roleta *___'+ mesa +'___\n*♟ Estrategia* ___'+estrategia+'___',parse_mode= 'Markdown')

        sinalConfirmado,estrategia = verificaSinalConfirmado()
        if sinalConfirmado == True:
            
            clientes = selecionaTodosClientes()
            for cliente in clientes:
                updater.bot.send_message(int(cliente['chat_id']), '*✅ Jogada confirmada*\n\n* 🎰 Roleta *___'+ mesa +'___\n*♟ Estrategia* ___'+estrategia+'___\n*⚡️ Entrada* Nomear entradas',parse_mode= 'Markdown')


    # print(str(sinal['roulette']) + ' ' + str(sinal['value']))    



    #clientes = selecionaTodosClientes()
    #for cliente in clientes:
    #    updater.bot.send_message(int(cliente['chat_id']), 'teste')








