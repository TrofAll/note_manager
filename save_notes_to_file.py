# Импортируем модуль из библиотеки
from datetime import datetime

# Создаем функцию
def save_notes_to_file (notes, filename):
    # Открываем файл для записи, определяем кодировку
    with open(filename, 'w', encoding='utf-8') as file:
        for note in notes:
            content = f"Имя пользователя: {note['username']}\n"
            content += f"Заголовок: {note['title']}\n"
            content += f"Описание: {note['content']}\n"
            content += f"Статус: {note['status']}\n"
            content += f"Дата создания: {note['created_date']}\n"
            content += f"Дедлайн: {note['issue_date']}\n"
            content += f"\n---\n"
            file.write(content)
if __name__ == '__main__':
    # Получаем текущую дату и время и преобразуем в строку
    current_date = str(datetime.now())
    # Пример списка заметок
    notes = [
    {'username': 'Александр',
    'title': 'Список дел',
    'content': 'Посетить спортзал',
    'status': 'новая',
    'created_date': '30.01.2025',
    'issue_date': '30.02.2025'},
    ]

    # Вызываем функцию для сохранения списка заметок
    save_notes_to_file(notes, "notes.txt")