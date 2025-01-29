# Загрузка заметок из файла
# Обработка ошибок
# Создаем функцию, которая принимает аргумент
def load_notes_from_file(filename):
    # Создаем пустой список
    notes = []
    # Создаем таблицу преобразования ключей
    translate_table = {
        "Имя пользователя": "username",
        "Заголовок": "title",
        "Описание": "content",
        "Статус": "status",
        "Дата создания": "created_date",
        "Дедлайн": "issue_date"
    }
    # Запускаем блок на проверку ошибок (Задание 3)
    try:
        # Открываем файл для чтения с требуемой кодировкой
        with open(filename, "r", encoding='utf-8') as file:
            # Читаем содержимое файла
            content = file.read()
            if content:
                # Разделяем содержимое на блоки заметок по разделителю
                note_blocks = content.split("\n---\n")
                # Проходим по каждому блоку заметок
                for block in note_blocks:
                    # Разделяем блоки на строки
                    note_lines = block.split("\n")
                    # Создаем новый пустой словарь для хранения данных заметки
                    note = {}
                    # Проходим по каждой строке в блоке
                    for line in note_lines:
                        # Проверяем, содержит ли строка разделитель ": "
                        if ": " in line:
                            # Разделяем строку на ключ и значение
                            verbose_key, value = line.split(": ", 1)
                            # Преобразуем русский ключ в английский с помощью таблицы для преобразования
                            key = translate_table[verbose_key]
                            # Добавляем пару ключ-значение в словарь заметки
                            note[key] = value
                    # Добавляем заметку в список заметок
                    notes.append(note)
    # Обработка ошибок, если файл не найден (Задание 3)
    except FileNotFoundError:
        print(f"Файл '{filename}' файл не найден, создайте файл.")
    # Обработка любых других ошибок (Задание 3)
    except Exception as e:
        print(f"Произошла ошибка чтения файла: {e}")

    # Возвращаем список заметок
    return notes

if __name__ == '__main__':
    # Загружаем заметки из файла
    notes = load_notes_from_file("notes.txt")
    # Проходим по каждой заметки и выводим её на экран
    for note in notes:
        print(note)