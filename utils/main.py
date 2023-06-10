# Из файла functions.py импортируем необходимые функции
from functions import open_json_file, load_operations_dates, load_where_paid, load_transfer_amount

last_operation = open_json_file()

# Запускаем цикл и выводим необходимую информацию о платежах в нужном формате
for operation in last_operation:
    print(f"{load_operations_dates(operation['date'])} {operation['description']}")
    print(f"{load_where_paid(operation)}", end='')
    print(f"{load_transfer_amount(operation)}")
    print()
