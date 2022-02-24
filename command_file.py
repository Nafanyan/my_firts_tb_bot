
from storage_users import*
import work_status_users as wsu


def users_msg(update, context):
    text = update.message.text
    id = str(update.effective_user.id)
    try:
        result = int(text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{result}')
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Я не совсем понимаю')

def hi_command(update, context):
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update, context):
    id = str(update.effective_user.id)
    output_str = ''
    user_base = read_storage()
    for i in user_base[id]:
        output_str += f'{i}\n'
    update.message.reply_text(f'{output_str} ')

def start(update, context):
    id = str(update.effective_user.id)
    output_str = ''
    user_base = read_storage()
    if (not (id in user_base)):
        add_new_user(id)
        wsu.new_user_status(id)
    for i in user_base[id]:
        output_str += f'{i}\n'
    update.message.reply_text(f'Приветствую! \nВот список команд, доступный для использования:\n{output_str}')












