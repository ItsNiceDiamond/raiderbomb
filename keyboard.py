# Created by Delitel
from telebot import types
import random
import cfg

def buy_keyboard():
    emoji = "❤🧡💛💚💙💜🖤❣💕💞💓💗💖💝"
    random_emoji = random.choice(emoji)
    buy_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buy_keyboard.add("Получить доступ"+random_emoji)
    buy_keyboard.add("ℹ️Помощь")
    return buy_keyboard

def buy_keyboard_inline(user_id):
    buy_keyboard_inline = types.InlineKeyboardMarkup()
    buy_keyboard_inline_1 = types.InlineKeyboardButton(text = "Оплатить", url=cfg.QIWI_LINK+str(user_id)+"-sms&blocked[0]=sum&blocked[1]=comment&blocked[2]=account")
    buy_keyboard_inline_2 = types.InlineKeyboardButton(text = "Проверить оплату", callback_data="check_pay")
    buy_keyboard_inline.add(buy_keyboard_inline_1)
    buy_keyboard_inline.add(buy_keyboard_inline_2)
    return buy_keyboard_inline

home_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
home_keyboard.add("Бомбер 📨","Руководство 🧾")
home_keyboard.add("ℹ️Помощь")


cancel_keyboard = types.InlineKeyboardMarkup()
cancel_keyboard_1 = types.InlineKeyboardButton(text = "Отмена❌", callback_data="cancel")
cancel_keyboard.add(cancel_keyboard_1)


admin_panel = types.InlineKeyboardMarkup()
admin_panel_1 = types.InlineKeyboardButton(text = "Ползователи👥",callback_data="users")
admin_panel_2 = types.InlineKeyboardButton(text = "Админы👑",callback_data="admins")
admin_panel_3 = types.InlineKeyboardButton(text = "Рассылка✉️",callback_data="mailing")
admin_panel_4 = types.InlineKeyboardButton(text = "Выдать доступ к боту📲",callback_data="give_acces")
admin_panel.add(admin_panel_1,admin_panel_2)
admin_panel.add(admin_panel_3)
admin_panel.add(admin_panel_4)

admin_panel_admins = types.InlineKeyboardMarkup()
admin_panel_admins_1 = types.InlineKeyboardButton(text="Просмотреть список админов📃",callback_data="admins_list")
admin_panel_admins_2 = types.InlineKeyboardButton(text="Добавить админа✅",callback_data="add_admin")
admin_panel_admins_3 = types.InlineKeyboardButton(text = "Удалить админа❌",callback_data="remove_admin")
admin_panel_admins_4 = types.InlineKeyboardButton(text="Отмена",callback_data="cancel_adm")
admin_panel_admins.add(admin_panel_admins_1)
admin_panel_admins.add(admin_panel_admins_2,admin_panel_admins_3)
admin_panel_admins.add(admin_panel_admins_4)

cancel_keyboard_adm = types.InlineKeyboardMarkup()
cancel_keyboard_1 = types.InlineKeyboardButton(text = "Отмена❌", callback_data="cancel_adm")
cancel_keyboard_adm.add(cancel_keyboard_1)

#mailing_keyboard = types.InlineKeyboardMarkup()
#mailing_keyboard_1 = types.InlineKeyboardButton(text="Всем👥",callback_data="all")
#mailing_keyboard_2 =types.InlineKeyboardButton(text="С доступом🤩",callback_data="with_acces")
#mailing_keyboard_3 =types.InlineKeyboardButton(text="Без доступа🤓",callback_data="not_acces")
#mailing_keyboard.add(mailing_keyboard_1)
#mailing_keyboard.add(mailing_keyboard_2,mailing_keyboard_3)