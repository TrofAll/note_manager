username = input('Введите ваше имя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Текущий статус: ')
created_date = input('Начало заметки (в формате день-месяц-год): ')
issue_date = input('Окончание заметки (в формате день-месяц-год): ')
title_1 = input('Введите заголовок заметки 1: ')
title_2 = input('Введите заголовок заметки 2: ')
title_3 = input('Введите заголовок заметки 3: ')
title_0 = [title_1, title_2, title_3]
note = [username, title, content, status, created_date, issue_date, title_0]
print(note)