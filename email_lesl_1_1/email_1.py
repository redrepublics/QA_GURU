from datetime import date
import math
#Задание 1. Создание словаря email
email = {
    "subject": "Отчёт за неделю",
    "from": "ivan@example.com",
    "to": "petr@example.com",
    "body": "Добрый день! Отправляю отчёт за прошедшую неделю."
}

#Задание 2. Создаем дату отправки
send_date = date.today().strftime("%Y-%m-%d")
email["date"] = send_date

# Задание 3. Нормализация email адресов отправителя и получаетля. Убарием регистры и лишние пробелы
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

#Задание 4. Извлекаем логин и домен отправителя в две переменные
login = email["from"].split("@")[0]
domain =email["from"].split("@")[1]

#Задание 5. Делаем сокращенную версию текста, первые 10 символов, затем  ...
email['short_body'] = email['body'][:10] + "..."

#Задание 6. Создаем два спсика доменов (делаем прямой копипас из задания). Проверяем на дубли.
personal_domains = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
corporate_domains = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
personal_domains = list(dict.fromkeys(personal_domains))
corporate_domains = list(dict.fromkeys(corporate_domains))

#Задание 7. Проверяем что нет пересечений, не один домен не должен входитьв  оба списка одновременно.
#В случае нахождения домена, выводим тот который дублируется в обоих списках
no_intersection = not (set(personal_domains) & set(corporate_domains))


# Задание 8. Проверка корпоративных отправителей.
sender_domain = email["from"].split("@")[0]
is_corporate = sender_domain in corporate_domains

# Задание 9. Сборка чистого текста сообщения. Сначала символ переноса, потом табуляцию.
email['clean_body'] = email['body'].replace("\n", " ").replace("\t", " ")

# Задание 10. Формируем текст отправляемого письма
email["sent_text"] = f"""Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}, дата {email["date"]} 

{email["clean_body"]}"""


#Задание 11. Расчет страниц печати из расчета 500 символов на 1 страницу
pages = (len(email["sent_text"]) + 499) // 500

# Задание 12. Проверка пустоты темы и тела письма.
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["clean_body"].strip()



# Задание 13. Создать маску и записать в переменную
login, domain = email["from"].split("@")
email['masked_from'] = f'{login[:2]}***@{domain}'

# Задание 14. Удаляем два домена из списка
personal_domains = [
    domain for domain in personal_domains
    if domain not in ["list.ru", "bk.ru"]
]

#Выводим ключевой результат
print(email)
print(is_corporate, pages, is_subject_empty, is_body_empty)