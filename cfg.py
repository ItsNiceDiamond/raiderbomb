# Created by Delitel
import hashlib
import os.path


# # # # # # # # # # ОСНОВНЫЕ ДАННЫЕ # # # # # # # # # # # # # # ##
token = "1228547810:AAHExdtyLbjabkx5xtzh-7AFDBUDdg4rtO8"  # Токен бота телеграм берём у @BotFather
QIWI_NUM = "+380994984332"  # Номер нашего киви кошелька
QIWI_token = "24bd5bf0808190752182415b5236dc32" # токен QIWI
AMOUNT = "35"  # Сумма которую пользователь будет должен оплатить чтобы получить доступ к боту (писать просто число)
operator = "894779913"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
QIWI_LINK = 'https://qiwi.com/payment/form/99?extra[%27account%27]=' + QIWI_NUM + '&amountInteger=' + AMOUNT + '&amountFraction=00&extra[%27comment%27]='  # Это трогать не нужно!!!



def create_admins_list():
    exists = os.path.exists("admins.txt")
    if not exists:
        with open("admins.txt", "a") as f:
            pass


def create_users_list():
    exists = os.path.exists("users.txt")
    if not exists:
        with open("users.txt", "a") as f:
            pass


def create_users_sub_list():
    exists = os.path.exists("users_sub.txt")
    if not exists:
        with open("users_sub.txt", "a") as f:
            pass


def create_users_unsub_list():
    exists = os.path.exists("users_unsub.txt")
    if not exists:
        with open("users_unsub.txt", "a") as f:
            pass
