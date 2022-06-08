
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup 
from telegram.ext import CallbackQueryHandler
from telegram.ext.updater import Updater # Conter a chave da api vinda do botfather
from telegram.update import Update # Isso será invocado toda vez que um bot receber uma atualização
from telegram.ext.callbackcontext import CallbackContext # Não usaremos sua funcionalidade diretamente em nosso código, mas quando adicionarmos o dispatcher, será necessário (e funcionará internamente)
from telegram.ext.commandhandler import CommandHandler #Esta classe Handler é usada para lidar com qualquer comando enviado pelo usuário ao bot, um comando sempre começa com “/” ou seja, “/start”,”/help” etc.
from telegram.ext.messagehandler import MessageHandler #Esta classe Handler é usada para lidar com qualquer mensagem normal enviada pelo usuário ao bot
from telegram.ext.filters import Filters # Isso filtrará texto normal, comandos, imagens, etc. de uma mensagem enviada.

from dados import resultadoSinal,inserirSinal,confirmaSinal,SelecionaSinalExistente,inserirNovoUsuario,SelecionaTodasRoletas,SelecionaEstrategias, SelecionaTodosSinais
from src.estrategia import encontrarEstrategia

print('Telegram bot inicializado')

telegram = Updater("5350481212:AAEpiE5l-qYkEommV2AvQ5oBUS1-qt9jqSQ", use_context=True)

roletas = []

def iniciar():   
    mensagem = "*Seja bem-vindo(a)*\n\n" 
    mensagem = "*ATENÇÂO 🚨*\n\n___O Robo esta iniciando a analise das roletas___\n\n"
    #telegram.bot.send_message(782375549,mensagem,parse_mode= 'Markdown')
  
    sinaisEmAndamento = []

    while(True):

        tiposRoletas = SelecionaTodasRoletas()
        
        # Pega todos os tipos de roletas
        for roletas in tiposRoletas:

            # pega todas as roletas
            for roleta in roletas['roletas']:

                #iniciar captura dos sinais e analisa a roleta
                roleta = roleta['nome'].replace(' ','-')
                sinais = SelecionaTodosSinais(roleta)

                interromper = False
                sinaisTratados = []

                for sinal in sinais:
                    if(interromper == False):
                        try:
                            sinaisTratados.append(sinal['value'])
                        except:
                            interromper = True
                            resultadoSinal(roletas['nome'],roleta, 5 )
                
                  
                bolas = [0,0,0,0,0,0,0,0,0,0,0,0]
                
                for sinal in sinaisTratados:
                    bolas = encontrarEstrategia(sinal,bolas)


                estrategias = SelecionaEstrategias()

                # LEGENDA DO ARRAY DE BOLAS
                # 0 - Vermelho | 1 - Preto | 2 - Impar
                # 3 - Par | 4 - Alto | 5 - Baixo
                # 6 - Duzia 1 | 7 - Duzia 2 | 8 - Duzia 3
                # 9 - Coluna 1 | 10 - Coluna 2 | Coluna 3

                # Analisa se bate com alguma estrategia =============================
                print(bolas)

                # Verificar se ja existe algum sinal em andamento 
                sinalEmAndamento = SelecionaSinalExistente(roletas['nome'],roleta.replace('-',' '))
                status = 0
                jogadasAntiga = 0

                for sinalAndamento in sinalEmAndamento:
                    status = sinalAndamento['status']
                    if status == 2:
                        jogadasAntiga = sinalAndamento['jogadas']
                
                ## ANALISA OS SINAIS ======================
                if status == 0:
                    analisaMesa(roletas['nome'],estrategias,bolas,roleta)

                ## COMFIRMA ENTRADA ======================
                if status == 1:
                    confirmaEntrada(roletas['nome'],estrategias,bolas,roleta,len(sinaisTratados))

                ## VERIFICA WIN x LOSS ========================
                if status == 2:
                    confirmaWin(roletas['nome'],estrategias,bolas,roleta,len(sinaisTratados),jogadasAntiga)

               
        time.sleep(10)
        #print(roletas)
        


def confirmaWin(tipo,estrategias,bolas,roleta,jogadas,jogadasAntiga):

    if(jogadas > jogadasAntiga):

        loss = True

        for estrategia in estrategias:
            
            # REPETICAO
            if(estrategia['estrategia'].split('-')[0] == 'r'):

                ## REPETINDO VERMELHO ===========================
                if(estrategia['estrategia'].split('-')[1] == 'v'):
                    
                    ## WIN OU LOSS
                    if(estrategia['confirma'] < bolas[0]):
                        resultadoSinal(tipo,roleta, 3)
                        loss = False
                 
                    

                ## REPETINDO PRETO ===========================
                if(estrategia['estrategia'].split('-')[1] == 'p'):
                 
                  ## WIN OU LOSS
                    if(estrategia['confirma'] < bolas[1]):
                        resultadoSinal(tipo,roleta, 3 )
                        loss = False
                    
        if loss == True:
            resultadoSinal(tipo,roleta, 4 )


def confirmaEntrada(tipo,estrategias,bolas,roleta,jogadas):
    
    for estrategia in estrategias:
        
        # REPETICAO
        if(estrategia['estrategia'].split('-')[0] == 'r'):

            ## REPETINDO VERMELHO ===========================
            if(estrategia['estrategia'].split('-')[1] == 'v'):
                ## ANALISANDO REPETICAO DO VERMELHO
                if(estrategia['confirma'] == bolas[0]):
                    confirmado(tipo,roleta, 'Repeticao do vermelho',estrategia['aposta'],jogadas)

            ## REPETINDO PRETO ===========================
            if(estrategia['estrategia'].split('-')[1] == 'p'):
                ## ANALISANDO REPETICAO DO VERMELHO
               # if(estrategia['confirma'] == bolas[1]):
                if(3 == bolas[1]):
                    confirmado(tipo,roleta, 'Repeticao do preto',estrategia['aposta'],jogadas)



def analisaMesa(tipo,estrategias,bolas,roleta):
    
    for estrategia in estrategias:
        
        # REPETICAO
        if(estrategia['estrategia'].split('-')[0] == 'r'):

            ## REPETINDO VERMELHO ===========================
            if(estrategia['estrategia'].split('-')[1] == 'v'):
                ## ANALISANDO REPETICAO DO VERMELHO
                if(estrategia['analise'] == bolas[0]):
                    analisando(roletas['nome'],roleta, 'Repeticao do vermelho')

            ## REPETINDO PRETO ===========================
            if(estrategia['estrategia'].split('-')[1] == 'p'):
                ## ANALISANDO REPETICAO DO VERMELHO
                if(estrategia['analise'] == bolas[1]):
                    analisando(tipo,roleta, 'Repeticao do preto')
          
        




def analisando(tipo,roleta,estrategia):
    mensagem = "⏱️ *ANALISANDO MESA*\n\n"
    mensagem += "🎰 *ROLETA* ___"+roleta.replace('-',' ')+"___\n"
    mensagem += "♟ *ESTRATEGIA* ___"+estrategia+"___"
    telegram.bot.send_message(782375549,mensagem,parse_mode= 'Markdown' )
    inserirSinal(tipo,roleta.replace('-',' '))


     
   
def confirmado(tipo,roleta,estrategia,aposta,jogadas): 
   
    entrada = ""

    if(aposta == "a-v"):
        entrada = "Apostar no vermelho"

    if(aposta == "a-p"):
        entrada = "Apostar no preto"
   
   
    mensagem = "✅ *JOGADA CONFIRMADA*\n\n"
    mensagem += "🎰 *ROLETA* ___"+roleta.replace('-',' ')+"___\n"
    mensagem += "♟ *ESTRATEGIA* ___"+estrategia+"___\n"
    mensagem += "⚡️*ENTRADA*: ___" + entrada +"___"
    telegram.bot.send_message(782375549,mensagem,parse_mode= 'Markdown' )
    confirmaSinal(tipo,roleta,jogadas)


iniciar()


# inicializar o processo do BOT
#def start(update: Update, context: CallbackContext):
    
    #
    #update.message.reply_text(mensagem,parse_mode= 'Markdown' )
    #mensagem = "*ATENÇÂO 🚨*\n\n___Projeto em estagio de criação___\n\n"
    #update.message.reply_text(mensagem,parse_mode= 'Markdown' )
    #inserirNovoUsuario(update.message.chat_id) # Cadastrar novo usuario

##
##updater.dispatcher.add_handler(CommandHandler('start', start))
##updater.start_polling()



