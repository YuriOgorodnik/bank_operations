Проект: Операции по банковским счетам клиента.

Авторство: Огородник Юрий Александрович.

Назначение проекта: Проект предназначен для хранения и обработки данных об операциях клинта по банковским счетам,
а также оперативного предоставления информации о 5 (пяти) последних успешных операциях.

Программное обеспечение, библиотеки: 
- Язык программирования: Python (3.7 и выше);
- Библиотеки: attrs, colorama, coverage, iniconfig, packaging, pluggy, pytest, pytest-cov, pip.

Функция считывания данных и вывода последних 5 (пяти) операций:

def open_json_file():

    """
    Получает отсортированные данные из json-файла
    об успешных операциях клиента по счетам и выводит
    на экран список из 5 (пяти) последних выполненных
    операций 
    """

    directory_path = os.path.abspath('D:/course_work_3/utils')
    file_path = os.path.join(directory_path, 'operations.json')
    with open(file_path, 'r', encoding='UTF-8') as file:
        all_operations = json.load(file)
        last_operations = filter(lambda item: item.get("date") and item["state"] == "EXECUTED", all_operations)
        last_operations = sorted(last_operations, key=lambda item: item["date"])[:-6:-1]
    return last_operations

Процедура тестирования: В качестве процедуры тестирования было использовано pytest. Все написанные тесты можно найти
по адресу: tests/tests_functions.py

Установка и использование проекта:
- Скачайте исходный код с GitHub;
- Установите зависимости, запустите pip install -r requirements.txt;
- Запустите проект с помощью команды python main.py

