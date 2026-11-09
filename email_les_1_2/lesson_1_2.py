from datetime import date


# 1. Нормализация email
def normalize_email(address):
    return address.strip().lower()


# 2. Создание короткого текста
def create_short_body(body):
    return body[:10] + "..."


# 3. Очистка тела письма
def clean_body(body):
    return body.replace("\n", " ").replace("\t", " ").strip()


# 4. Маскировка email
def mask_email(address):
    login, domain = address.split("@")
    return login[:2] + "***@" + domain


# 5. Проверка корректности email
def check_email(address):
    if address.count("@") != 1:
        return False

    login, domain = address.split("@")

    if not login or not domain:
        return False

    if not domain.endswith((".com", ".ru", ".net")):
        return False

    return True


# 6. Создание словаря письма
def create_email(subject, sender, recipient, send_date, body):
    return {
        "subject": subject,
        "from": sender,
        "to": recipient,
        "date": send_date,
        "body": body
    }


# 7. Формирование итогового текста письма
def create_email_text(email):
    return (
        f"Кому: {email['to']}, от {email['masked_from']}\n"
        f"Тема: {email['subject']}, дата {email['date']}\n\n"
        f"{email['clean_body']}"
    )


# 8. Главная функция отправки письма
def send_email(recipients, subject, message, sender):

    # 1. Проверяем список получателей
    if not recipients:
        raise ValueError("Список получателей пуст")

    # 2. Нормализуем email
    sender = normalize_email(sender)
    recipients = [normalize_email(r) for r in recipients]

    # 3. Проверяем корректность адресов
    if not check_email(sender):
        raise ValueError("Некорректный email отправителя")

    for recipient in recipients:
        if not check_email(recipient):
            raise ValueError(f"Некорректный email: {recipient}")

    # 4. Проверяем тему и сообщение
    subject = subject.strip()
    message = clean_body(message)

    if not subject or not message:
        raise ValueError("Тема и сообщение не должны быть пустыми")

    # 5. Исключаем отправку самому себе
    recipients = [r for r in recipients if r != sender]

    # 6. Подготавливаем общие данные
    send_date = date.today().strftime("%Y-%m-%d")
    masked_from = mask_email(sender)
    short_body = create_short_body(message)

    # 7. Создаём письмо для каждого получателя
    result = []

    for recipient in recipients:
        email = create_email(
            subject,
            sender,
            recipient,
            send_date,
            message
        )

        email["masked_from"] = masked_from
        email["short_body"] = short_body
        email["clean_body"] = message

        # 8. Формируем итоговый текст
        email["email_text"] = create_email_text(email)

        result.append(email)

    return result

letters = send_email(
    recipients=[
        "USER1@gmail.com",
        "USER2@mail.ru",
        "vladislav@gmail.com"
    ],
    subject="Тестовое письмо",
    message="Привет! Это тестовое сообщение.",
    sender="vladislav@gmail.com"
)

for letter in letters:
    print(letter["email_text"])
    print("-" * 50)