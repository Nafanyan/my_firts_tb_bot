from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from storage_users import*



def hi_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/city \n ')


def start(update: Update, context: CallbackContext) -> None:
    id = str(update.effective_user.id)
    output_str = ''
    user_base = read_storage()
    if (not (id in user_base)): add_new_user(id)
    for i in user_base[id]:
        output_str += f'{i}\n'
    update.message.reply_text(f'Приветствую! \nВот список команд, доступный для использования:\n{output_str}')

