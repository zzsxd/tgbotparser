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
from backend import TempUserData


def main():

    @bot.message_handler(commands=['adduser'])
    def send_question(message):
        print(message)
        user_id = message.from_user.id
        command = message.text.replace('/', '')
        if command == 'adduser' and user_id in config.get_config()['admins']:
            temp_data.temp_data(user_id)[user_id][0] = True
            bot.send_message(group_id, 'Введите ID нового человека')

    @bot.message_handler(content_types=['text'])
    def text(message):
        user_input = message.text
        user_id = message.from_user.id
        if temp_data.temp_data(user_id)[user_id][0]:
            if user_input is not None:
                try:
                    config.update_users(int(user_input))
                    temp_data.temp_data(user_id)[user_id][0] = False
                    bot.send_message(group_id, 'Пользователь успешно добавлен')
                except:
                    bot.send_message(group_id, 'Ошибка добавления')
            else:
                bot.send_message(group_id, 'Это не текст')

    # Обработчик сообщений от администратора
    @bot.message_handler(func=lambda message: message.from_user.id in config.get_config()['users'])
    def forward_message_to_group(message):
        print(2323)
        bot.forward_message(group_id, message.chat.id, message.message_id)

    @bot.message_handler(func=lambda message: message.reply_to_message is not None and message.from_user.id in config.get_config()['users'])
    def forward_reply_to_group(message):
        bot.forward_message(group_id, message.chat.id, message.reply_to_message.message_id)
        bot.forward_message(group_id, message.chat.id, message.message_id)

    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    temp_data = TempUserData()
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()