# Created by Delitel
import sqlite3
import re
import cfg, telebot, keyboard

bot = telebot.TeleBot(cfg.token)

conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user 
    (user_id INTEGER, status INTEGER)''')
c.execute(('''CREATE TABLE IF NOT EXISTS mailer_temporality
    (user_id INTEGER,mailer_text TEXT,recipient TEXT)'''))
c.execute('''CREATE TABLE IF NOT EXISTS sms_bomber_status
    (user_id INTEGER,status INTEGER,number TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS count_attack
    (user_id INTEGER,count INTEGER)''')
conn.commit()
conn.close()


def add_to_database(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    res = c.execute("SELECT * FROM user WHERE user_id=?",(user_id,)).fetchone()
    try:
        check = res[1]
    except:
        c.execute("INSERT INTO user VALUES(?,?)",(user_id,0))
        check = 0
        conn.commit()
    res_2 = c.execute("SELECT * FROM count_attack WHERE user_id=?",(user_id,)).fetchone()
    try:
        res_1 =res_2[1]
    except:
        c.execute("INSERT INTO count_attack VALUES(?,?)",(user_id,0,))
        res_1 = 0
        conn.commit()
    conn.close()
    with open("users.txt") as f:
        x = f.read()
        if str(user_id) in x:
            pass
        else:
            with open("users.txt","a") as f:
                f.write(str(user_id)+"\n")
    with open("users_sub.txt") as f:
        y = f.read()
        if str(user_id) in y:
            pass
        else:
            with open ("users_unsub.txt") as f:
                d = f.read()
                if str(user_id) in d:
                    pass
                else:
                    with open("users_unsub.txt","a") as f:
                        f.write(str(user_id)+"\n")
    return check, res_1


def set_sub_status(user_id):
    conn = sqlite3.connect("users.db")
    c =conn.cursor()
    c.execute("UPDATE user SET status=? WHERE user_id=?",(1,user_id,))
    conn.commit()
    conn.close()
    with open("users_sub.txt") as f:
        x = f.read()
        if str(user_id) in x:
            pass
        else:
            with open("users_sub.txt", "a") as f:
                f.write(str(user_id)+"\n")

    with open("users_unsub.txt") as f:
        lines = f.readlines()
    string = str(user_id)
    pattern = re.compile(re.escape(string))
    with open("users_unsub.txt", 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)


def get_sms_bomber_status(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    res = c.execute("SELECT * FROM sms_bomber_status WHERE user_id=?",(user_id,)).fetchone()
    conn.close()
    try:
        return res[1],res[2]
    except:
        return "NONE","NONE"


def set_sms_bomber_status(user_id,status,number):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("UPDATE sms_bomber_status SET status=? WHERE user_id=?",(status,user_id,))
    c.execute("UPDATE sms_bomber_status SET number=? WHERE user_id=?",(number,user_id,))
    conn.commit()
    conn.close()

def add_sms_bomber_status(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("DELETE FROM sms_bomber_status WHERE user_id=?",(user_id,))
    conn.commit()
    c.execute("INSERT INTO sms_bomber_status VALUES(?,?,?)",(user_id,1,"NONE",))
    conn.commit()
    conn.close()

def act_count_attack(act,user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    if act == "add":
        res = c.execute("SELECT * FROM count_attack WHERE user_id=?", (user_id,)).fetchone()
        after_count = res[1] + 1
        c.execute("UPDATE count_attack SET count=? WHERE user_id=?", (after_count, user_id,))
        conn.commit()
    elif act == "remove":
        res = c.execute("SELECT * FROM count_attack WHERE user_id=?",(user_id,)).fetchone()
        after_count = res[1] - 1
        c.execute("UPDATE count_attack SET count=? WHERE user_id=?",(after_count,user_id,))
        conn.commit()
    conn.close()

def get_count_attack(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    res = c.execute("SELECT * FROM count_attack WHERE user_id=?",(user_id,)).fetchone()
    conn.close()

    return res[1]

def get_info_admin():
    with open("admins.txt") as f:
        x = f.read()
    return x

def count_users():
    with open("users.txt") as f:
        x = f.readlines()
    return len(x)

def count_admins():
    with open("admins.txt") as f:
        x = f.read()
    with open("admins.txt") as f:
        y = f.readlines()
    return len(y),x

def set_status(user_id, status):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("UPDATE user SET status=? WHERE user_id=?",(status,user_id,))
    conn.commit()
    conn.close()

def action_with_admin(action,user_id):
    if action == "add":
        with open("admins.txt", "a") as f:
            f.write(user_id+"\n")
    elif action == "remove":
        with open("admins.txt") as f:
            lines = f.readlines()
        str = user_id
        pattern = re.compile(re.escape(str))
        with open("admins.txt", 'w') as f:
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    f.write(line)

def mailing(user_id,text):
    with open("users.txt") as f:
        ban = 0
        send = 0
        while True:
            x = f.readline()
            if x == "":
                bot.send_message(user_id,"Рассылка закончена🥳\n\nОтправлено: "+str(send)+" сообщений!\nЗаблокировано: "+str(ban)+" сообщений!",reply_markup=keyboard.admin_panel)
                break
            else:
                try:
                    bot.send_message(x,text)
                    send += 1
                except:
                    ban += 1