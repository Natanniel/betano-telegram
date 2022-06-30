
import time
from cv2 import log
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackQueryHandler
# Conter a chave da api vinda do botfather
from telegram.ext.updater import Updater
# Isso será invocado toda vez que um bot receber uma atualização
from telegram.update import Update
# Não usaremos sua funcionalidade diretamente em nosso código, mas quando adicionarmos o dispatcher, será necessário (e funcionará internamente)
from telegram.ext.callbackcontext import CallbackContext
# Esta classe Handler é usada para lidar com qualquer comando enviado pelo usuário ao bot, um comando sempre começa com “/” ou seja, “/start”,”/help” etc.
from telegram.ext.commandhandler import CommandHandler
# Esta classe Handler é usada para lidar com qualquer mensagem normal enviada pelo usuário ao bot
from telegram.ext.messagehandler import MessageHandler
# Isso filtrará texto normal, comandos, imagens, etc. de uma mensagem enviada.
from telegram.ext.filters import Filters

from dados import resultadoSinal, excluirSinais, inserirSinal, confirmaSinal, SelecionaSinalExistente, inserirNovoUsuario, SelecionaTodasRoletas, SelecionaEstrategias, SelecionaTodosSinais
from src.estrategia import  repeticaoVermelho, analisaConfirmacao

print('Telegram bot inicializado')

telegram = Updater(
    "5350481212:AAEpiE5l-qYkEommV2AvQ5oBUS1-qt9jqSQ", use_context=True)

roletas = []

sinaisEmAndamento = []
# 0 - ChatID
# 1 - MessageID
# 2 - Sinal
# 3 - Roleta
# 4 - Gale
# 5 - confirma
# 6 - Entrada confirmada


def iniciar():
    mensagem = "*ATENÇÂO 🚨*\n\n___O Robo esta iniciando a analise das roletas___\n\n"
    telegram.bot.send_message(782375549, mensagem, parse_mode='Markdown')

    while(True):

        # Pega todos os tipos de roletas
        tiposRoletas = SelecionaTodasRoletas()
        for roletas in tiposRoletas:

            # pega todas as roletas
            for roleta in roletas['roletas']:

                # iniciar captura dos sinais e analisa a roleta
                nomeRoleta = roleta['nome']
                sinais = roleta['resultados'][::-1]
                analisandoRoleta = False
                analise = []

                # Verifica se a roleta esta em analise
                for andamento in sinaisEmAndamento:
                    if andamento[3] == nomeRoleta:
                        analisandoRoleta = True
                        analise = andamento

                if(analisandoRoleta == True):
                    # Ja sinalizou analisando mesa
                    #
                    entradaConfirmada, apagarMensagem, Green = analisaConfirmacao(
                        analise, sinais)

                    if(apagarMensagem == True):
                        if(apagarMensagem and analise[7] == 1):
                            mensagemLoss(analise)
                        else:
                            apagarMensagemEnviada(analise, sinais)

                    if(entradaConfirmada == True and analise[7] == 0):
                        EnviarMensagemJogadaConfirmada(analise)

                    if(Green):
                        EnviarMensagemVitoria(analise)

                else:

                    # Iniciar analise de sinais X estrategias
                    estrategiaEncontrada = []
                    estrategias = SelecionaEstrategias()

                    estrategiaEncontrada = repeticaoVermelho(
                        sinais, estrategias)

                    if(len(estrategiaEncontrada) > 0):
                        enviarMensagemAnalisa(
                            estrategiaEncontrada[0], nomeRoleta)

        time.sleep(5)


def enviarMensagemAnalisa(estrategia, nomeRoleta):

    nomeEstrategia = retornaEstrategia(estrategia['estrategia'])

    mensagem = "⏳ *ANALISANDO MESA* ⏳ \n\n"
    mensagem += "🎲 *𝑹𝒐𝒍𝒆𝒕𝒂* 🎰: ___" + nomeRoleta + "___\n"
    mensagem += "♟*𝑬𝒔𝒕𝒓𝒂𝒕𝒆́𝒈𝒊𝒂*: " + nomeEstrategia

    x = telegram.bot.send_message(-1001710936639,
                                  mensagem, parse_mode='Markdown')

    sinaisEmAndamento.append([-1001710936639, x.message_id, estrategia['estrategia'],
                             nomeRoleta, 0, estrategia['confirma'], estrategia['aposta'], 0])


def mensagemLoss(estrategia):
    mensagem = "❌ LOSS!\n\nFaz parte do jogo,\n SEGUE O GERENCIAMENTO."
    telegram.bot.send_message(-1001710936639, mensagem,
                              reply_to_message_id=estrategia[0], parse_mode='Markdown')
    novaEstrategias = []

    global sinaisEmAndamento
    for sinalAndamento in sinaisEmAndamento:
        if(sinalAndamento[0] != estrategia[0] and sinalAndamento[1] != estrategia[1] and sinalAndamento[2] != estrategia[2] and sinalAndamento[3] != estrategia[3] and sinalAndamento[4] != estrategia[4] and sinalAndamento[5] != estrategia[5]):
            novaEstrategias.append(sinalAndamento)

    sinaisEmAndamento = novaEstrategias
    excluirSinaisAnteriores(estrategia)


def EnviarMensagemVitoria(estrategia):

    mensagem = "✅🤑🟢 WIN !\n\nVEM COM A EASY MONEY 🟢 🙅‍♂️✅"
    telegram.bot.send_message(-1001710936639, mensagem,
                              reply_to_message_id=estrategia[0], parse_mode='Markdown')
    novaEstrategias = []

    global sinaisEmAndamento
    for sinalAndamento in sinaisEmAndamento:
        if(sinalAndamento[0] != estrategia[0] and sinalAndamento[1] != estrategia[1] and sinalAndamento[2] != estrategia[2] and sinalAndamento[3] != estrategia[3] and sinalAndamento[4] != estrategia[4] and sinalAndamento[5] != estrategia[5]):
            novaEstrategias.append(sinalAndamento)

    sinaisEmAndamento = novaEstrategias
    excluirSinaisAnteriores(estrategia)


def apagarMensagemEnviada(estrategia, sinais):
    telegram.bot.delete_message(estrategia[0], estrategia[1])

    novaEstrategias = []
    global sinaisEmAndamento
    for sinalAndamento in sinaisEmAndamento:
        if(sinalAndamento[0] != estrategia[0] and sinalAndamento[1] != estrategia[1] and sinalAndamento[2] != estrategia[2] and sinalAndamento[3] != estrategia[3] and sinalAndamento[4] != estrategia[4] and sinalAndamento[5] != estrategia[5]):
            novaEstrategias.append(sinalAndamento)

    sinaisEmAndamento = novaEstrategias


def excluirSinaisAnteriores(estrategia):
    excluirSinais(estrategia[3])

# 0 - ChatID
# 1 - MessageID
# 2 - Sinal
# 3 - Roleta
# 4 - Gale
# 5 - confirma


def EnviarMensagemJogadaConfirmada(estrategia):
    nomeEstrategia = retornaEstrategia(estrategia[2])
    entrada = reetornaEstrategiaEntrada(estrategia[6])

    mensagem = "🧬 *𝑱𝑶𝑮𝑨𝑫𝑨 𝑪𝑶𝑵𝑭𝑰𝑹𝑴𝑨𝑫𝑨* 🧬\n\n"
    mensagem += "🎲 *𝑹𝒐𝒍𝒆𝒕𝒂* 🎰 ___"+estrategia[3] + "___\n"
    mensagem += "♟ *𝑬𝒔𝒕𝒓𝒂𝒕𝒆́𝒈𝒊𝒂* ___"+nomeEstrategia+"___\n"
    mensagem += "⚡️𝑬𝒏𝒕𝒓𝒂𝒅𝒂: ___" + entrada+"___\n\n"
    mensagem += "___(𝑪𝒐𝒃𝒓𝒊𝒓 𝒐 𝒁𝑬𝑹𝑶 0️⃣)___"
    x = telegram.bot.send_message(-1001710936639,
                                  mensagem, parse_mode='Markdown')

    novaEstrategias = []
    global sinaisEmAndamento
    for sinalAndamento in sinaisEmAndamento:
        if(sinalAndamento[0] == estrategia[0] and sinalAndamento[1] == estrategia[1] and sinalAndamento[2] == estrategia[2] and sinalAndamento[3] == estrategia[3] and sinalAndamento[4] == estrategia[4] and sinalAndamento[5] == estrategia[5]):
            sinalAndamento[7] = 1
            sinalAndamento[0] = x.message_id
            novaEstrategias.append(sinalAndamento)
        else:
            novaEstrategias.append(sinalAndamento)
    sinaisEmAndamento = novaEstrategias
    excluirSinaisAnteriores(estrategia)


def reetornaEstrategiaEntrada(estrategia):
    entrada = ''

    match estrategia:
        case 'a-v':
            entrada = "Apostar no Vermelho"
        case 'a-p':
            entrada = "Apostar no Preto"
        case 'a-np':
            entrada = "Apostar em Pares"
        case 'a-ni':
            entrada = "Repetição em Impares"
        case 'a-na':
            entrada = "Apostar numeros Altos"
        case 'a-nb':
            entrada = "Apostar numeros Baixos"
        case 'a-d1':
            entrada = "Apostar 1° Duzia"
        case 'a-d2':
            entrada = "Apostar 2° Duzia"
        case 'a-d3':
            entrada = "Apostar 3° Duzia"
        case 'a-d1d2':
            entrada = "Apostar 1° e 2° Duzia"
        case 'a-d2d3':
            entrada = "Apostar 2° e 3° Duzia"
        case 'a-d1d3':
            entrada = "Apostar 1° e 3° Duzia"
        case 'a-c1':
            entrada = "Apostar 1° Coluna"
        case 'a-c2':
            entrada = "Apostar 2° Coluna"
        case 'a-c3':
            entrada = "Apostar 3° Coluna"
        case 'a-c1dc':
            entrada = "Apostar 1° e 2° Coluna"
        case 'a-c2c3':
            entrada = "Apostar 2° e 3° Coluna"
        case 'a-c1c3':
            entrada = "Apostar 1° e 3° Coluna"

    return entrada


def retornaEstrategia(estrategia):
    entrada = ''

    match estrategia:
        case 'r-v':
            entrada = "Repetição do Vermelho"
        case 'r-p':
            entrada = "Repetição do Preto"
        case 'r-np':
            entrada = "Repetição de Pares"
        case 'r-ni':
            entrada = "Repetição de Impares"
        case 'r-na':
            entrada = "Repetição numeros Altos"
        case 'r-nb':
            entrada = "Repetição numeros Baixos"
        case 'r-d1':
            entrada = "Repetição 1° Duzia"
        case 'r-d2':
            entrada = "Repetição 2° Duzia"
        case 'r-d3':
            entrada = "Repetição 3° Duzia"
        case 'r-c1':
            entrada = "Repetição 1° Coluna"
        case 'r-c2':
            entrada = "Repetição 2° Coluna"
        case 'r-c3':
            entrada = "Repetição 3° Coluna"

    return entrada


iniciar()
