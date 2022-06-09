
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup 
from telegram.ext import CallbackQueryHandler
from telegram.ext.updater import Updater # Conter a chave da api vinda do botfather
from telegram.update import Update # Isso será invocado toda vez que um bot receber uma atualização
from telegram.ext.callbackcontext import CallbackContext # Não usaremos sua funcionalidade diretamente em nosso código, mas quando adicionarmos o dispatcher, será necessário (e funcionará internamente)
from telegram.ext.commandhandler import CommandHandler #Esta classe Handler é usada para lidar com qualquer comando enviado pelo usuário ao bot, um comando sempre começa com “/” ou seja, “/start”,”/help” etc.
from telegram.ext.messagehandler import MessageHandler #Esta classe Handler é usada para lidar com qualquer mensagem normal enviada pelo usuário ao bot
from telegram.ext.filters import Filters # Isso filtrará texto normal, comandos, imagens, etc. de uma mensagem enviada.

from dados import inserirNovoUsuario

print('Telegram bot inicialiado')

updater = Updater("5350481212:AAEpiE5l-qYkEommV2AvQ5oBUS1-qt9jqSQ", use_context=True)

# inicializar o processo do BOT
def start(update: Update, context: CallbackContext):
    mensagem = "*Seja bem-vindo(a)*\n\n" 
    mensagem = "*ATENÇÂO 🚨*\n\n___O Robo esta iniciando a analise das roletas___\n\n"
    print(update.message.chat_id)
    #telegram.bot.send_message(782375549,mensagem,parse_mode= 'Markdown')
  
    update.message.reply_text(mensagem,parse_mode= 'Markdown' )
    inserirNovoUsuario(update.message.chat_id) # Cadastrar novo usuario



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()




