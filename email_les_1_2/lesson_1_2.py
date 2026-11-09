from email_lesl_1_1.email_1 import email
from datetime import date

##Часть A. Функции Создайте набор функций для обработки информации о письме. Каждая функция должна выполнять ровно одно действие и возвращать результат.

# 1. Нормализация email адресов - приводит адреса к нижнему регистру и убирает пробелы

def normalize_email(address):
    return address.strip().lower()
# Нормализуем адреса и записываем обратно в словарь
email["from"] = normalize_email(email["from"])
email["to"] = normalize_email(email["to"])

# 2. Сокращенная версия тела письма - создает короткую версию тела (первые 10 символов + "...")
def create_short_body(email):
    email["short_body"] = email["body"][:10] + "..."

create_short_body(email)

# 3. Очистка текста письма - заменяет табы и переводы строк на пробелы
def clean_body(body):
    return body.replace("\n", " ").replace("\t", " ")

email["clean_body"] = clean_body(email["body"])

# 4. Формирование итогового текста письма - создает форматированный текст письма
def create_email_text(email):
    return (
        f"Кому: {email['to']}, от {email['from']}\n"
        f"Тема: {email['subject']}, дата {email['date']}\n\n"
        f"{email['clean_body']}"
    )

# 6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)
def mask_email(address):
    login, domain = address.split("@")
    return login[:2] + "***@" + domain


email["masked_from"] = mask_email(email["from"])

# 7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)
def check_email(address):
    if "@" not in address:
        return False

    if not address.endswith((".com", ".ru", ".net")):
        return False

    return True

# 8. Создание словаря письма - создает базовую структуру письма
def create_email(subject, sender, recipient, date, body):
    return {
        "subject": subject,
        "from": sender,
        "to": recipient,
        "date": date,
        "body": body
    }

# 9. Добавление даты отправки - добавляет текущую дату

def date_time():
    send_date = date.today().strftime("%Y-%m-%d")
    return send_date

email["date"] = date_time()

# 10. Получение логина и домена - разделяет email на логин и домен
def extract_login_domain(email):
    login, domain = email["from"].split("@")
    return login, domain