# Данный скрипт является заданием к уроку https://school.qa.guru/pl/teach/control/lesson/view?id=350245561&editMode=0
import datetime

# Обьявляем переменные

subj = 'Str'
send_mail = 'Str1'
to = 'Str2'
send_data = datetime.datetime.now().strftime('%Y-%m-%d')

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

print(clean_personal_domains)
print(clean_corporate_domains)


#
# # Проверяем оба списка на предмет повторов. Поскольку по умолчанию ТЗ нет, считаем что эталонным должен быть первый
# # список
# def not_duplication(clean_personal, clean_corporate):
#     return not set(clean_personal).intersection(set(clean_corporate))
#     if  not_duplication(clean_corporate, clean_corporate) == set():
#         return True
#     else:
#         return False
# print(not_duplication(personal_domains, corporate_domains))




#
#
# # Обьявляем словарь заготовку
# mail_dict = {
#     "subject": {subj},
#     "from": {send_mail},
#     "to": {to},
#     "date": {send_data}
# }
#
# print(mail_dict)