import pytest
from utils import functions


def test_open_json_file():
    assert functions.open_json_file() is not None


def test_load_payment_description():
    assert functions.load_payment_description() == ['Открытие вклада', 'Перевод организации', 'Перевод организации',
                                                    'Перевод со счета на счет', 'Открытие вклада']
    assert type(functions.load_payment_description()) != 'dict'


@pytest.fixture
def operations():
    all_operations = [
        {
            'id': 1,
            'date': '2017-01-01T12:00:00',
            'description': 'Operation 2',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 21344.35, 'currency': {'name': 'руб.'}},
            'state': 'EXECUTED'

        },
        {
            'id': 2,
            'date': '2018-01-01T12:00:00',
            'description': 'Operation 2',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {
            'id': 3,
            'date': '2015-01-01T12:00:00',
            'description': 'Operation 3',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {
            'id': 4,
            'date': '2020-01-01T12:00:00',
            'description': 'Operation 4',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {},
        {
            'id': 5,
            'date': '2021-01-01T12:00:00',
            'description': 'Operation 5',
            'operationAmount': {'amount': 100, 'currency': {'name': 'RUB'}},
            'state': 'EXECUTED'
        },
        {
            'id': 6,
            'date': '2022-01-01T12:00:00',
            'description': 'Operation 6',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        }

    ]
    return all_operations


def test_load_operations_dates(operations):
    assert functions.load_operations_dates(operations[1]['date']) == "01.01.2018"
    assert functions.load_operations_dates('2021-01-01T12:00:00') == '01.01.2021'


def test_load_transfer_amount(operations):
    assert functions.load_transfer_amount(operations[0]) == "21344.35 руб."
    assert functions.load_transfer_amount(operations[1]) != "100 руб."


def test_load_where_paid(operations):
    assert functions.load_where_paid(operations[3]) == 'Account **A -> Account **B\n'
