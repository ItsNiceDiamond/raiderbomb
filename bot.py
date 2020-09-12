# -*- coding: utf-8 -*-
# Created by Delitel
import telebot
import cfg, db, keyboard
import requests
import json
import random
import bomber
import threading
import time

cfg.create_admins_list()
cfg.create_users_list()
cfg.create_users_sub_list()
cfg.create_users_unsub_list()

bot = telebot.TeleBot(cfg.token)


@bot.message_handler(content_types=["text"])
def message_handler(message):
    if message.text:
        sms_status = db.get_sms_bomber_status(message.chat.id)
        status = db.add_to_database(message.chat.id)
        if sms_status[0] == 1:
            if message.text[0:3] == "380" and len(message.text) == 12 or message.text[0:2] == "79" and len(message.text) == 11:
                db.add_sms_bomber_status(message.chat.id)
                db.set_sms_bomber_status(message.chat.id,2,message.text)
                bot.send_message(message.chat.id,"Введите время <b>*в секундах*</b> на которое хотите оставить спам:",parse_mode="html",reply_markup=keyboard.cancel_keyboard)
            else:
                bot.send_message(message.chat.id,"Вы ввели неправельный номер!",reply_markup=keyboard.cancel_keyboard)
        elif sms_status[0] == 2:
            seconds = list(range(1,1801))
            try:
                if int(message.text) in seconds:
                    threading.Thread(target=bomber.bomber, args=(message.chat.id,message.text,sms_status[1])).start()
                    db.set_sms_bomber_status(message.chat.id,"NONE","NONE")
                else:
                    bot.send_message(message.chat.id,"Вы можете оставить спам от 1 до 1800 секунд!")
            except:
                bot.send_message(message.chat.id, "Вы можете оставить спам от 1 до 1800 секунд!")
        elif status[0] == "add_admin":
            res = db.get_info_admin()
            if str(message.text) in res:
                bot.send_message(message.chat.id, "Админ уже есть в списке!\nВведите другой <b>user_id!</b>",parse_mode="html", reply_markup=keyboard.cancel_keyboard_adm)
            else:
                db.action_with_admin("add", message.text)
                db.set_status(message.chat.id, 1)
                bot.send_message(message.chat.id, "Готово!", reply_markup=keyboard.admin_panel_admins)


        elif status[0] == "remove_admin":
            res = db.get_info_admin()
            if str(message.text) in res:
                if message.text == str(message.chat.id):
                    bot.send_message(message.chat.id,"Вы не можете удалить самого себя!\nВведите другой <b>user_id</b>!",reply_markup=keyboard.cancel_keyboard_adm, parse_mode="html")
                else:
                    db.action_with_admin("remove", message.text)
                    db.set_status(message.chat.id, 1)
                    bot.send_message(message.chat.id, "Готово!", reply_markup=keyboard.admin_panel_admins)
            else:
                bot.send_message(message.chat.id, "Админ отстутствует!\nВведите другой <b>user_id</b>!",parse_mode="html", reply_markup=keyboard.cancel_keyboard_adm)
        elif status[0] == "mailing":
            threading.Thread(target=db.mailing, args=(message.chat.id, message.text)).start()
            bot.send_message(message.chat.id, "Рассылка начата!")
            db.set_status(message.chat.id, 1)
        elif status[0] == "give_acces":
            try:
                bot.send_message(message.text,"Вам был выдан доступ к боту🥳\n\nНажмите 👉🏻<b>/start</b>👈🏻 если меню не появилось!",parse_mode="html", reply_markup=keyboard.home_keyboard)
                db.set_sub_status(message.text)
                bot.send_message(message.chat.id,"Готово!",reply_markup=keyboard.admin_panel)
                db.set_status(message.chat.id,0)
            except:
                bot.send_message(message.chat.id,"Ошибка!\n\nВозможно такого пользователя нет в базе данных!",reply_markup=keyboard.cancel_keyboard_adm)
        else:
            if message.text == "/start":
                if status[0] == 1:
                    bot.send_message(message.chat.id,"<code>Добро пожаловать!</code>\n\nЕсли кнопки управления не появились нажмите👉🏻<b>/start</b>👈🏻",parse_mode="html",reply_markup=keyboard.home_keyboard)
                else:
                    buy_keyboard = keyboard.buy_keyboard()
                    bot.send_message(message.chat.id,"Для приобретения доступа к боту воспользуйтесь меню!\n\nЕсли меню не появилось нажмите 👉🏻<b>/start</b>👈🏻",reply_markup=buy_keyboard,parse_mode="html")
            elif message.text == "/get_my_id":
                bot.send_message(message.chat.id,"Твой user_id: <code>"+str(message.chat.id)+"</code>",parse_mode="html")
            elif message.text == "/adm":
                info = db.get_info_admin()
                if str(message.chat.id) in info:
                    bot.send_message(message.chat.id,"Доступ получен!",reply_markup=keyboard.admin_panel)
                else:
                    bot.send_message(message.chat.id,"Доступ запрещён!")
            elif "Получить доступ" in message.text:
                buy_keyboard_inline = keyboard.buy_keyboard_inline(message.chat.id)
                bot.send_message(message.chat.id,"1️⃣ Для получения доступа к боту нажмите на кнопку "
                                                 "<code>\"Оплатить\"</code> снизу👇(Открывать через браузер, "
                                                 "<u><b>НЕ ЧЕРЕЗ ПРИЛОЖЕНИЕ</b></u>) и подтверждайте платёж! ("
                                                 "<u><b>менять поля не нужно, всё уже указано</b></u>)\n\n2️⃣ После "
                                                 "оплаты возращайтесь в бота и нажмите на кнопку <code>\"Проверить "
                                                 "оплату\"</code> и если вы всё сделали правильно бот автоматически "
                                                 "выдаст вам доступ!",parse_mode="html",reply_markup=buy_keyboard_inline)
            elif message.text == "ℹ️Помощь":
                emoji = "❤🧡💛💚💙💜🖤"
                random_emoji = random.choice(emoji)
                bot.send_message(message.chat.id,random_emoji+" Смс отправляются с более чем 40 разных сайтов (49 сервисов)\n\n"+random_emoji+" Доступ к боту выдается <code>навсегда</code>\n\n"+random_emoji+" Одновременный спам на 3 номера\n\n"+random_emoji+" Полная анонимность при использовании\n\n\n"+random_emoji+" Цена - <code>"+cfg.AMOUNT+"</code>р\n\nПо всем вопросам обращаться в лс:\n"+cfg.operator,parse_mode="html")
            elif message.text == "Бомбер 📨":
                count = db.get_count_attack(message.chat.id)
                if status[0] == 1:
                    if count >= 3:
                        bot.send_message(message.chat.id,"Вы не можете делать больше 3 атак одновременно!")
                    else:
                        db.add_sms_bomber_status(message.chat.id)
                        bot.send_message(message.chat.id,"Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx",reply_markup=keyboard.cancel_keyboard)
                else:
                    bot.send_message(message.chat.id,"Доступ запрещён!")
            elif message.text == "Руководство 🧾":
                bot.send_message(message.chat.id,"После покупки доступа к боту у вас появится новое меню под полем для ввода!\n\n1) Нажмите на кнопку <code>\"Бомбер 📨\"</code>\n2) Введите номер вашей жертвы(формат ввода будет приведён в сообщении от бота)\n3) Введите время <code>в секундах</code> на которое хотите оставить спам!\n4) Готово!\n\n<u>Бот оповестит вас когда спам начнётся и закончится!</u>",parse_mode="html")
            else:
                if status[0] == 1:
                    bot.send_message(message.chat.id,"<code>Добро пожаловать!</code>\n\nЕсли кнопки управления не появились нажмите👉🏻<b>/start</b>👈🏻",parse_mode="html",reply_markup=keyboard.home_keyboard)
                else:
                    buy_keyboard=keyboard.buy_keyboard()
                    bot.send_message(message.chat.id,"Для приобретения доступа к боту воспользуйтесь меню!\n\nЕсли меню не появилось нажмите 👉🏻<b>/start</b>👈🏻",parse_mode="html",reply_markup=buy_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.message:
        if call.data == "check_pay":
            s = requests.Session()
            s.headers['authorization'] = 'Bearer ' + cfg.QIWI_token
            parameters = {'rows': '10'}
            h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + cfg.QIWI_NUM + '/payments',params=parameters)
            s = parameters
            req = json.loads(h.text)
            for i in range(len(req['data'])):
                if req['data'][i]['comment'] == str(call.message.chat.id)+"-sms":
                    if req['data'][i]['sum']['amount'] == int(cfg.AMOUNT):
                        db.set_sub_status(call.message.chat.id)
                        bot.send_message(call.message.chat.id,"Доступ получен✅",reply_markup=keyboard.home_keyboard)
        elif call.data == "cancel":
            bot.send_message(call.message.chat.id,"Отмена❌")
            db.set_sms_bomber_status(call.message.chat.id,"NONE","NONE")
        elif call.data == "users":
            check_admin = db.get_info_admin()
            if str(call.message.chat.id) in check_admin:
                count = db.count_users()
                bot.send_message(call.message.chat.id, "Всего пользователей: " + str(count),reply_markup=keyboard.admin_panel)
            else:
                bot.send_message(call.message.chat.id, "Доступ запрещён!")
        elif call.data == "admins":
            bot.edit_message_text("Выберите действие:", call.message.chat.id, call.message.message_id,reply_markup=keyboard.admin_panel_admins)
        elif call.data == "admins_list":
            count = db.count_admins()
            bot.send_message(call.message.chat.id,"Всего админов: <code>" + str(count[0]) + "</code>\n\n<u>Список:</u> \n<b>" + str(count[1]) + "</b>\n\nТвой user_id: <code>" + str(call.message.chat.id) + "</code>",parse_mode="html", reply_markup=keyboard.admin_panel_admins)
        elif call.data == "add_admin":
            check_admin = db.get_info_admin()
            if str(call.message.chat.id) in check_admin:
                db.set_status(call.message.chat.id, "add_admin")
                bot.edit_message_text("Введите <b>user_id</b> пользователя:", call.message.chat.id,call.message.message_id, reply_markup=keyboard.cancel_keyboard_adm, parse_mode="html")
            else:
                bot.send_message(call.message.chat.id, "Доступ запрещён!")
        elif call.data == "remove_admin":
            check_admin = db.get_info_admin()
            if str(call.message.chat.id) in check_admin:
                db.set_status(call.message.chat.id, "remove_admin")
                bot.edit_message_text("Введите <b>user_id</b> пользователя:", call.message.chat.id,call.message.message_id, reply_markup=keyboard.cancel_keyboard_adm, parse_mode="html")
            else:
                bot.send_message(call.message.chat.id, "Доступ запрещён!")
        elif call.data == "mailing":
            check_admin = db.get_info_admin()
            if str(call.message.chat.id) in check_admin:
                db.set_status(call.message.chat.id, "mailing")
                bot.edit_message_text("Рассылыку получат все!\nВведите текст рассылки:", call.message.chat.id,call.message.message_id, reply_markup=keyboard.cancel_keyboard_adm)
            else:
                bot.send_message(call.message.chat.id, "Доступ запрещён!")
        elif call.data == "cancel_adm":
            bot.send_message(call.message.chat.id,"Отмена❌",reply_markup=keyboard.admin_panel)
            db.set_status(call.message.chat.id,1)
        elif call.data == "give_acces":
            check_admin = db.get_info_admin()
            if str(call.message.chat.id) in check_admin:
                bot.edit_message_text("Введите <b>user_id</b> пользователя которому хотите выдать доступ:", call.message.chat.id,call.message.message_id, reply_markup=keyboard.cancel_keyboard_adm, parse_mode="html")
                db.set_status(call.message.chat.id,"give_acces")
            else:
                bot.send_message(call.message.chat.id, "Доступ запрещён!")

while True:
	try:
		bot.polling()
	except:
		time.sleep(10)