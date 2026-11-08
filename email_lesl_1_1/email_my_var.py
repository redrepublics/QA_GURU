
from datetime import date
import math


# Исходные данные и переменные
email = {
    "subject": "Отчёт за неделю",
    "from": "ivan@example.com",
    "to": "petr@example.com",
    "body": "Добрый день! Отправляю отчёт за прошедшую неделю."
}

personal_domains = [
    "gmail.com", "list.ru", "yahoo.com", "outlook.com",
    "hotmail.com", "icloud.com", "yandex.ru", "mail.ru",
    "list.ru", "bk.ru", "inbox.ru"
]

corporate_domains = [
    "company.ru", "corporation.com", "university.edu",
    "organization.org", "company.ru", "business.net"
]

CHARS_PER_PAGE = 500
DOMAINS_TO_REMOVE = ["list.ru", "bk.ru"]


# Функции

# Нормализует email-адрес: удаляет пробелы по краям
# и переводит все символы в нижний регистр.
def normalize_email(address):
    return address.strip().lower()


# Удаляет повторяющиеся домены из списка,
# сохраняя первоначальный порядок элементов.
def remove_duplicates(domains):
    return list(dict.fromkeys(domains))


# Проверяет, является ли строка пустой
# или содержит только пробелы.
# Возвращает True, если строка пустая, иначе False.
def is_empty(text):
    return not text.strip()


# Извлекает домен из email-адреса.
# Например, из ivan@example.com возвращает example.com.
def get_domain(address):
    return address.split("@")[1]


# Очищает текст от символов табуляции и переноса строки,
# заменяя их обычными пробелами.
def clean_text(text):
    return text.replace("\t", " ").replace("\n", " ")


# Формирует полный текст отправленного письма
# из получателя, отправителя, темы, даты и тела сообщения.
def create_email_text(email):
    return (
        f"Кому: {email['to']}, от {email['from']}\n"
        f"Тема: {email['subject']}, дата {email['date']}\n\n"
        f"{email['clean_body']}"
    )


# Создаёт маску email-адреса:
# оставляет первые два символа логина,
# заменяет остальные на *** и сохраняет домен.
# Например: ivan@example.com → iv***@example.com.
def create_mask(address):
    login, domain = address.split("@")
    return f"{login[:2]}***@{domain}"


# 1–5. Обработка исходных данных
email["date"] = date.today().strftime("%Y-%m-%d")
email["from"] = normalize_email(email["from"])
email["to"] = normalize_email(email["to"])
email["short_body"] = email["body"][:10] + "..."


# 6–8. Проверка доменов
personal_domains = remove_duplicates(personal_domains)
corporate_domains = remove_duplicates(corporate_domains)

common_domains = set(personal_domains) & set(corporate_domains)
no_intersection = not common_domains

is_corporate = get_domain(email["from"]) in corporate_domains


# 9–10. Подготовка письма
email["clean_body"] = clean_text(email["body"])
email["sent_text"] = create_email_text(email)


# 11–13. Дополнительные проверки и обработка
pages = math.ceil(len(email["sent_text"]) / CHARS_PER_PAGE)

is_subject_empty = is_empty(email["subject"])
is_body_empty = is_empty(email["clean_body"])

email["masked_from"] = create_mask(email["from"])


# 14. Удаление ненужных личных доменов
personal_domains = [
    domain for domain in personal_domains
    if domain not in DOMAINS_TO_REMOVE
]


# Вывод результатов
print(email)
print(f"Количество страниц: {pages}")
print(f"Корпоративный отправитель: {is_corporate}")
print(f"Пересечений доменов нет: {no_intersection}")
print(f"Общие домены: {common_domains}")
print(f"Тема пустая: {is_subject_empty}")
print(f"Тело письма пустое: {is_body_empty}")
print(f"Личные домены после очистки: {personal_domains}")
