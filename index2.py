
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


updater = Updater("5453075884:AAFIhjRHkLQe0CgDgd_HQjZrJHFQUcl_OqU", use_context=True)
#updater = Updater("5350481212:AAEpiE5l-qYkEommV2AvQ5oBUS1-qt9jqSQ", use_context=True)


def recepcionar(update: Update, context: CallbackContext):
    
    print(update.channel_post.text)
    try:
        print(update.channel_post.text)
        if update.channel_post.text.split(' ')[0] == 'init':
            mensagem = "*Seja bem-vindo(a)*\n\n" 
            mensagem += "*✅ Registrado*\n___Canal registrado com sucesso !___\n\n"
            update.channel_post.sender_chat.send_message(mensagem,parse_mode= 'Markdown' )
            
            time.sleep(10)
            update.message.delete()
            inserirNovoUsuario(update.message.chat_id)
    except:
        print("CRITICO AQUI " + update.channel_post.chat_id + ' ' + print(update.channel_post.chat_id))
   
#updater.bot.send_message(-1001568564951,"Teste")

#updater.bot.
   ## 
   ## mensagem = "*ATENÇÂO 🚨*\n\n___O Robo esta iniciando a analise das roletas___\n\n"
    
    #telegram.bot.send_message(782375549,mensagem,parse_mode= 'Markdown')
  
   ## update.message.reply_text(mensagem,parse_mode= 'Markdown' )
    # Cadastrar novo usuario

updater.dispatcher.add_handler(MessageHandler(Filters.text, recepcionar))

updater.start_polling()




