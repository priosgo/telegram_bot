import os
token_bot = os.getenv('TTOKEN')
from telegram.ext import Updater, CommandHandler
from telegram.forcereply import ForceReply
from telegram.ext.filters import Filters
from telegram.ext.updater import Updater
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
import logging
from datetime import date, timedelta
from get_sales import get_sheets_sales
PAULO_ID=1115236899
CARLOS_ID=1359662327
OMAN_ID=1286728594
id_list = [PAULO_ID,CARLOS_ID,OMAN_ID]

updater = Updater(token_bot, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)
                     
def ventas(ventas, context):
    usr_id = ventas.message.from_user.id
    if usr_id in id_list:
        ventas.message.reply_text('Getting information...')
        ventas.message.reply_text('It could take a few seconds...')
        result = get_sheets_sales(ventas.message.text  )
        if (type(result) == list):
            ventas.message.reply_text('Sales information of  ' + result[0] + " " + ventas.message.text)
            ventas.message.reply_text('Purchases: ' + result[1])
            ventas.message.reply_text('Sales: ' + result[2])
        else:
            ventas.message.reply_text(ventas.message.text + ' it is not a valid date!')
    else:
        print("You don´t have permissions to read...")


def year(year, context):
    #actual_year = date.today().year
    #year.message.reply_text(actual_year)
    tienda = ("2020-08-29","2020-09-05","2020-09-12","2020-09-19","2020-09-26","2020-10-03","2020-10-10","2020-10-17","2020-10-24","2020-10-31","2020-11-07","2020-11-14","2020-11-21","2020-11-28","2020-12-05","2020-12-12","2020-12-19","2020-12-26")
    year.message.reply_text(tienda)
   

def start(update, context: CallbackContext):
    update.message.reply_text(
        'Welcome  {}'.format(update.message.from_user.first_name))
    update.message.reply_text('To get sales, please use date format as dd-mm-aa ')
    dispatcher.add_handler(MessageHandler(Filters.text, ventas, ForceReply))


init_param = CommandHandler('start', start)
# date_param = CommandHandler('year', year)
#sales = CommandHandler('', ventas)
#dispatcher.add_handler(sales)
dispatcher.add_handler(init_param)
#dispatcher.add_handler(date_param)
updater.start_polling()
updater.idle()
