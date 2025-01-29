# Формат файла json
# Импортируем библиотеку json
import json

# Создаем функцию сохранения заметок в json файл
def save_notes_json(notes, filename):
    # Запускаем блок ошибок
    try:
        # Открываем файл в режиме записи c автозакрытием после заершения
        with open(filename, "w", encoding='utf-8') as file:
            # Записываем заметки в формате json
            json.dump(notes, file, ensure_ascii=False, indent=4)
    # Обработка ошибки когда файл не найден
    except FileNotFoundError:
        print(f"Файл '{filename}' файл не найден, создайте файл.")
    # Обработка всех прочих ошибок
    except Exception as e:
        print(f"Произошла ошибка при записи в файл, побробуйте заново '{filename}': {e}")

if __name__ == '__main__':
    # Список ключей и значений
    notes_to_save = [
    {'username': 'Александр',
    'title': 'Список дел',
    'content': 'Посетить спортзал',
    'status': 'новая',
    'created_date': '30.01.2025',
    'issue_date': '30.02.2025'},
    ]

    # Вызываем функцию для сохранения заметок в файл
    save_notes_json(notes_to_save, "notes.json")