def send_email(message, recipient, *, sender='university.help@gmail.com'):      # определяем функцию и её аргументы
    dom_zone = (".com", ".ru", ".net")      # создаем кортеж из доменных зон
    if '@' not in recipient or '@' not in sender or not recipient.endswith(dom_zone) or not sender.endswith(dom_zone):      # проверка на корректность e-mail отправителя и получателя
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:       # проверка на отправку самому себе
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':         # проверка на отправителя по умолчанию
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
