#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
from telebot import types
#####################################
class Bot_inline_btns:
    def __init__(self):
        super(Bot_inline_btns, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=2)

    def msg_buttons(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        product_catalog = types.KeyboardButton('Каталог продуктов🗂')
        profile = types.KeyboardButton('Профиль👤')
        support = types.KeyboardButton('Поддержка👨‍💻')
        keyboard.add(product_catalog, profile, support)
        return keyboard