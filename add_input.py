username = input ('Введите ваше имя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Текущий статус: ')
created_date = input('Начало заметки (в формате день-месяц-год): ')
issue_date = input('Окончание заметки (в формате день-месяц-год): ')
print('Имя ползователя:',username)
print('Заголовок заметки:',title)
print('Описание заметки:',content)
print('Статус заметки:',status)
print('Дата начала:',created_date[0:5])
print('Дата завершения:',issue_date[0:5])