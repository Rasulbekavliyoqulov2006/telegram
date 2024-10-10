from abc import ABC, abstractmethod
import json
from datetime import datetime
import time
import random

telegram_language = input("english\nuzbek\nrussian\ntanlang->  ")

if telegram_language == "english":
    class Telegram:
        def __init__(self, user_name):
            self.user_name = user_name
            self.chat_text = ""
            self.chat_status = "idle"
            self.chat_time = None

        def register(self):
            phone_number = input("Enter your phone number: ")
            sms_code = random.randint(1000, 9999)
            print(f"An SMS code has been sent to your phone: {sms_code}")
            user_input = input("Enter the SMS code you received: ")
            return user_input == str(sms_code)

        def show_info(self):
            print(f"User Name: {self.user_name}")
            print(f"Chat Text: {self.chat_text if self.chat_text else 'No message'}")
            print(f"Chat Status: {self.chat_status}")
            print(f"Chat Time: {self.chat_time if self.chat_time else 'Time not set'}")
            print()

        def send(self, receiver, message):
            self.chat_text = message
            receiver.chat_text = message
            self.chat_time = datetime.now().strftime("%d -%b %H:%M:%S")
            receiver.chat_time = self.chat_time
            self.chat_status = "sending"
            receiver.chat_status = "received"
            print(f"Message from {self.user_name} to {receiver.user_name}: '{message}' sent.")

        def read(self):
            if self.chat_text:
                self.chat_status = "reading"
                print(f"{self.user_name} is reading their message: '{self.chat_text}'", datetime.now().strftime("%d -%b %H:%M:%S"))
            else:
                print(f"No messages for {self.user_name}.")

        def delete(self):
            if self.chat_text:
                confirm = input(f"{self.user_name}, do you want to delete the message? (yes/no): ").lower()
                if confirm == 'yes':
                    print(f"{self.user_name} deleted the message: '{self.chat_text}'")
                    self.chat_text = ""
                    self.chat_status = "idle"
                else:
                    print(f"{self.user_name} cancelled the deletion of the message.")
            else:
                print(f"No message to delete for {self.user_name}.")

        def show_chat(self):
            print(f"{self.user_name}'s messages:")
            print(f"Message: {self.chat_text if self.chat_text else 'No message'}\nTime: {self.chat_time if self.chat_time else 'Time not set'}")
            print()

        def search_user(self):
            user_search = input("Enter the name of the contact you are searching for: ")
            try:
                with open('contacts.json', 'r') as json_file:
                    contacts = json.load(json_file)
                found_contact = None
                for contact in contacts:
                    if contact["name"].lower() == user_search.lower():
                        found_contact = contact
                        break
                if found_contact:
                    print(f"Contact found: {found_contact['name']} - {found_contact['phone']}")
                    return Telegram(found_contact['name'])  
                else:
                    print("No such contact found.")
                    return None
            except FileNotFoundError:
                print("Contacts file not found.")
                return None

    user1 = Telegram(input("Enter your name: "))
    if user1.register():
        user2 = user1.search_user()

        if user2: 
            user1.send(user2, input("Enter your message: "))
            user2.read()
            time.sleep(5)
            user2.show_chat()
            user2.delete()  
            user2.show_chat()  
        else:
            print("Message sending process ended, user not found.")
    else:
        print("Registration failed.")

elif telegram_language == "uzbek":
    class Telegram:
        def __init__(self, nomi):
            self.nomi = nomi
            self.xabarlar = ""
            self.yozishmalar_holati = "bo'sh"
            self.suhbat_vaqti = None

        def royxatdan_otish(self):
            telefon_raqam = input("Telefon raqamingizni kiriting: ")
            sms_kod = random.randint(10000, 99999)
            print(f"Sizga SMS kod yuborildi: {sms_kod}")
            foydalanuvchi_raqam = input("Sizga yuborilgan SMS kodni kiriting: ")
            return foydalanuvchi_raqam == str(sms_kod)

        def malumotlarni_korish(self):
            print(f"Foydalanuvchi ismi: {self.nomi}")
            print(f"Xabar matni: {self.xabarlar if self.xabarlar else 'Xabar yo\'q'}")
            print(f"Xabar holati: {self.yozishmalar_holati}")
            print(f"Xabar vaqti: {self.suhbat_vaqti if self.suhbat_vaqti else 'Vaqt kiritilmagan'}")
            print()

        def xabar_jonatish(self, qabul_qiluvchi, xabar):
            self.xabarlar = xabar
            qabul_qiluvchi.xabarlar = xabar
            self.suhbat_vaqti = datetime.now().strftime("%d -%b %H:%M:%S")
            qabul_qiluvchi.suhbat_vaqti = self.suhbat_vaqti
            self.yozishmalar_holati = "jo'natilmoqda"
            qabul_qiluvchi.yozishmalar_holati = "qabul qilindi"

        def yozishmalarni_oqish(self):
            if self.xabarlar:
                self.yozishmalar_holati = "o'qilyapti"
                print(f"{self.nomi} o'ziga kelgan xabarni o'qiyapti: '{self.xabarlar}'", datetime.now().strftime("%d -%b %H:%M:%S"))
            else:
                print(f"{self.nomi} uchun xabar yo'q.")

        def ochirish(self):
            if self.xabarlar:
                confirm = input(f"{self.nomi}, xabarni o'chirishni xohlaysizmi? (ha/yo'q): ").lower()
                if confirm == 'ha':
                    print(f"{self.nomi} xabarni o'chirdi: '{self.xabarlar}'")
                    self.xabarlar = ""
                    self.yozishmalar_holati = "bo'sh"
                else:
                    print(f"{self.nomi} xabarni o'chirish rad etildi.")
            else:
                print(f"{self.nomi} uchun o'chiriladigan xabar yo'q.")

        def yozishmalarni_korish(self):
            print(f"{self.nomi}'ning xabarlari:")
            print(f"Xabar: {self.xabarlar if self.xabarlar else 'Xabar yo\'q'}\nVaqt: {self.suhbat_vaqti if self.suhbat_vaqti else 'Vaqt kiritilmagan'}")
            print()

        def kantakt_qidirish(self):
            profil_qidirish = input("Qidirayotgan kontakt ismini kiriting: ")
            try:
                with open('contacts.json', 'r') as fayl:
                    contacts = json.load(fayl)
                kantakt_qidirish = None
                for contact in contacts:
                    if contact["name"].lower() == profil_qidirish.lower():
                        kantakt_qidirish = contact
                        break
                if kantakt_qidirish:
                    print(f"Kantak topildi: {kantakt_qidirish['name']} - {kantakt_qidirish['phone']}")
                    return Telegram(kantakt_qidirish['name'])  
                else:
                    print("Bunday kontakt mavjud emas.")
                    return None
            except FileNotFoundError:
                print("Kontaktlar fayli topilmadi.")
                return None

    foydalanuvchi1 = Telegram(input("Ismingizni kiriting: "))
    if foydalanuvchi1.royxatdan_otish():
        foydalanuvchi2 = foydalanuvchi1.kantakt_qidirish()

        if foydalanuvchi2: 
            foydalanuvchi1.xabar_jonatish(foydalanuvchi2, input("Yubormoqchi bo'lgan matningizni kiriting: "))
            foydalanuvchi2.yozishmalarni_oqish()
            time.sleep(5)
            foydalanuvchi2.yozishmalarni_korish()
            foydalanuvchi2.ochirish()  
            foydalanuvchi2.yozishmalarni_korish()  
        else:
            print("Xabar yuborish jarayoni tugadi, foydalanuvchi topilmadi.")
    else:
        print("Royxatdan o'tish muvaffaqiyatsiz bo'ldi.")

elif telegram_language == "russian":
    class Telegram:
        def __init__(self, user_name):
            self.user_name = user_name
            self.chat_text = ""
            self.chat_status = "idle"
            self.chat_time = None

        def register(self):
            phone_number = input("Введите свой номер телефона: ")
            sms_code = random.randint(1000, 9999)
            print(f"SMS код был отправлен на ваш телефон: {sms_code}")
            user_input = input("Введите полученный SMS код: ")
            return user_input == str(sms_code)

        def show_info(self):
            print(f"Имя пользователя: {self.user_name}")
            print(f"Текст чата: {self.chat_text if self.chat_text else 'Нет сообщения'}")
            print(f"Статус чата: {self.chat_status}")
            print(f"Время чата: {self.chat_time if self.chat_time else 'Время не установлено'}")
            print()

        def send(self, receiver, message):
            self.chat_text = message
            receiver.chat_text = message
            self.chat_time = datetime.now().strftime("%d -%b %H:%M:%S")
            receiver.chat_time = self.chat_time
            self.chat_status = "sending"
            receiver.chat_status = "received"
            print(f"Сообщение от {self.user_name} к {receiver.user_name}: '{message}' отправлено.")

        def read(self):
            if self.chat_text:
                self.chat_status = "Чтение"
                print(f"{self.user_name} читает свое сообщение: '{self.chat_text}'", datetime.now().strftime("%d -%b %H:%M:%S"))
            else:
                print(f"Нет сообщений для {self.user_name}.")

        def delete(self):
            if self.chat_text:
                confirm = input(f"{self.user_name}, хотите удалить сообщение? (да/нет): ").lower()
                if confirm == 'да':
                    print(f"{self.user_name} удалил сообщение: '{self.chat_text}'")
                    self.chat_text = ""
                    self.chat_status = "idle"
                else:
                    print(f"{self.user_name} отменил удаление сообщения.")
            else:
                print(f"Нет сообщения для удаления у {self.user_name}.")

        def show_chat(self):
            print(f"Сообщения {self.user_name}:")
            print(f"Сообщение: {self.chat_text if self.chat_text else 'Нет сообщения'}\nВремя: {self.chat_time if self.chat_time else 'Время не установлено'}")
            print()

        def search_user(self):
            user_search = input("Введите имя контакта, который вы ищете: ")
            try:
                with open('contacts.json', 'r') as json_file:
                    contacts = json.load(json_file)
                found_contact = None
                for contact in contacts:
                    if contact["name"].lower() == user_search.lower():
                        found_contact = contact
                        break
                if found_contact:
                    print(f"Контакт найден: {found_contact['name']} - {found_contact['phone']}")
                    return Telegram(found_contact['name'])  
                else:
                    print("Такого контакта не найдено.")
                    return None
            except FileNotFoundError:
                print("Файл контактов не найден.")
                return None

    user1 = Telegram(input("Введите ваше имя: "))
    if user1.register():
        user2 = user1.search_user()

        if user2: 
            user1.send(user2, input("Введите ваше сообщение: "))
            user2.read()
            time.sleep(5)
            user2.show_chat()
            user2.delete()  
            user2.show_chat()  
        else:
            print("Процесс отправки сообщения завершен, пользователь не найден.")
    else:
        print("Регистрация не удалась.")

