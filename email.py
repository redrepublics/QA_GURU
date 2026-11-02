# Данный скрипт является заданием к уроку https://school.qa.guru/pl/teach/control/lesson/view?id=350245561&editMode=0
import datetime
from faker import Faker
import random
from pprint import pprint
import re
import json
import math
# Обьявляем переменные

send_data = datetime.datetime.now().strftime('%Y-%m-%d')
is_corporate = 'vladislav@company.ru'
clean_body = Faker().paragraph().replace("\t", " ").replace("\n", " ")
subj = 'Test subject'
login = 'red@'

# формирование письма с удалением лишних символов
sent_text_test = f"""
Добрый день!

Направляю вам информацию для ознакомления и дальнейшего рассмотрения.
В рамках текущей работы мы подготовили необходимые материалы, которые
позволят оценить текущее состояние проекта, определить основные задачи
и согласовать дальнейшие шаги.

Просьба ознакомиться с представленной информацией и сообщить, если
потребуются дополнительные пояснения или уточнения. Также будем
признательны за обратную связь по предложенным решениям и срокам
выполнения работ.

Предлагаю при необходимости организовать дополнительное обсуждение,
чтобы рассмотреть открытые вопросы, определить приоритеты и распределить
ответственность между участниками процесса.

Буду ожидать вашего ответа. Заранее благодарю за уделённое время
и сотрудничество!

С уважением,
Команда проекта.
"""
sent_text = re.sub(r'\s+', ' ', sent_text_test).strip()

# Списки персональных и интерпрайс доменов (примеры). Тут намеренно есть повторы, верхний регистр и пробелы
personal_domains = [' Gmail.com ','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
corporate_domains = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']

# Обрабатываем два списка на предмет верхнего регистра и пробелов.
# Выводим глобальные переменные, с уже исправленными значениями.

def clean_personal(personal_domains, corporate_domains):
    clean_personal_domains = str(personal_domains).strip().lower().replace(" ", "")
    clean_corporate_domains = str(corporate_domains).strip().lower().replace(" ", "")
    return clean_personal_domains, clean_corporate_domains


def remove_duplication(clean_personal_domains, clean_corporate_domains):

    # Преобразуем строки в списки
    clean_personal_domains = clean_personal_domains.strip("[]").replace("'", "").split(",")
    clean_corporate_domains = clean_corporate_domains.strip("[]").replace("'", "").split(",")

    # Удаляем дубликаты внутри списков
    clean_personal_domains = list(dict.fromkeys(clean_personal_domains))
    clean_corporate_domains = list(dict.fromkeys(clean_corporate_domains))

    # Удаляем пересечения между списками
    personal_set = set(clean_personal_domains)

    clean_corporate_domains = [
        domain for domain in clean_corporate_domains
        if domain not in personal_set
    ]

    return clean_personal_domains, clean_corporate_domains


# Сначала вызываем первую функцию
clean_personal_domains, clean_corporate_domains = clean_personal(
    personal_domains, corporate_domains
)

# Затем передаём её результат во вторую функцию
clean_personal_domains, clean_corporate_domains = remove_duplication(
    clean_personal_domains, clean_corporate_domains
)

# print(clean_personal_domains)
# print(clean_corporate_domains)

# Проверяем email на корпоративный домен
def is_corporate_fun(is_corporate, clean_corporate_domains):
    return is_corporate.split('@')[-1].lower() in clean_corporate_domains

is_corporate = is_corporate_fun(is_corporate, clean_corporate_domains)
# print(result)

# Формируем маску по ТЗ
masked_from = f'{login.split('@')[0][:2]}***@'
# Формируем маску
random_domain_corpoate = f'{masked_from}{random.choice(clean_corporate_domains)}'
ramdom_domain_personal = f'{masked_from}{random.choice(clean_personal_domains)}'


# print(random_domain_corpoate)

# # Обьявляем словарь заготовку
mail_dict = {
    "subject": subj,
    "from": random_domain_corpoate,
    "to": ramdom_domain_personal,
    "date": send_data,
    'clean_body': sent_text
}

mail_dict["sent_text"] = f"""Кому: {mail_dict["to"]}, от {mail_dict["from"]}
Тема: {mail_dict["subject"]}, дата {mail_dict["date"]}

{mail_dict["clean_body"]}"""
#Печатаем красивое письмо
print(mail_dict["sent_text"])

# Считаем кол-во страниц для печати и проверяем пустое ли письмо
if not sent_text.strip():
    print("Пустое письмо")
    is_body_empty = False
else:
    symbols_count = len(sent_text)
    pages = math.ceil(symbols_count / 500)
    print(f"\nНужно {pages} страниц для печати")
    is_body_empty = True

# Проверяем, пустая ли тема письма
if not subj.strip():
    is_subject_empty = False
else:
    is_subject_empty = True



# удаляем лишнее из списка персональных доменов

for domain in ['list.ru', 'bk.ru']:
    if domain in clean_personal_domains:
        clean_personal_domains.remove(domain)
if is_corporate == True:
    print("Входит в корпоративный список")
else:
    print('Входит в частный список, или не значится')


if is_body_empty == True:
    print('Письмо содержит данные')
else:
    print('Письмо пустое')

if is_body_empty == True:
    print('Есть тема сообщения')
else:
    print('Тема сообщения отсутсвует')