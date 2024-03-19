#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
config_name = 'secrets.json'
group_id = -1002062026726
#####################################
import os
import telebot
import platform
from frontend import Bot_inline_btns
from config_parser import ConfigParser

def main():
    # Обработчик сообщений от администратора
    @bot.message_handler(func=lambda message: message.from_user.id == 1897256227)
    def forward_message_to_group(message):
        bot.forward_message(group_id, message.chat.id, message.message_id)

    @bot.message_handler(func=lambda message: message.reply_to_message is not None and message.from_user.id == 1897256227)
    def forward_reply_to_group(message):
        bot.forward_message(group_id, message.chat.id, message.reply_to_message.message_id)
        bot.forward_message(group_id, message.chat.id, message.message_id)

    bot.polling(none_stop=True)

if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()