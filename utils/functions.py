# Импортируем необходимые для работы модули
import json
from datetime import datetime


def open_json_file():
    """
    Получает отсортированные данные из json-файла

    """
    with open('D:/course_work_3/utils/operations.json', 'r', encoding='UTF-8') as file:
        all_operations = json.load(file)
        last_operations = filter(lambda item: item.get("date") and item["state"] == "EXECUTED", all_operations)
        last_operations = sorted(last_operations, key=lambda item: item["date"])[:-6:-1]
    return last_operations


def load_operations_dates(operation_data):
    """
    Преобразовывает вывод даты операции в нужный формат

    """
    date = datetime.fromisoformat(operation_data)
    return date.strftime('%d.%m.%Y')


def load_payment_description():
    """
    Получает описание выполненного платежа

    """
    list_payment_description = []
    data = open_json_file()
    for description in data:
        list_payment_description.append(description['description'])
    return list_payment_description


def load_where_paid(operation):
    """
    Получает информацию о платеже (откуда и куда)

    """
    if operation.get('from') is not None:
        order_from, order_to = operation['from'].split(), operation['to'].split()
        order_from[-1], order_to[-1] = _hide_operation(order_from[-1]), \
                                       _hide_operation(order_to[-1])

        return " ".join(order_from) + " -> " + " ".join(order_to) + '\n'
    else:
        return ""


def load_transfer_amount(operation):
    """
    Получает информацию о сумме платежа и валюте

    """
    return f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"


def _hide_operation(operation):
    """
    Осуществляет вывод части номера карт и части номера счетов
    с применением спецсимволов (*) для поддержания информационной
    безопасности

    """
    if len(operation) == 16:
        return operation[:4] + " " + operation[4:6] + "" + "** " + "**** " + operation[12:16]
    else:
        return "**" + operation[len(operation) - 4:]


