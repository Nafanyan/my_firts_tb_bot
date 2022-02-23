from telegram import Update
from telegram import User
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import MessageHandler, Filters
from command_file import*

updater = Updater('5129629480:AAFUVifhSxk5grdrlQs2loTznpKElBZO1mg')

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), users_msg))
updater.dispatcher.add_handler(CommandHandler('hello', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('start', start))


print('Server Start')
updater.start_polling()
updater.idle()