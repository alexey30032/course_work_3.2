import json
from datetime import datetime


def get_list():
    """
    получение списка словарей из json
    """
    file_p = '../operations.json'
    with open(file_p) as file:
        data = json.load(file)
    return data


def sort_list(start_list):
    """
    сортировака списка по статусу платежа, далее по убыванию даты
    """
    unsorted_list = []
    for operation in start_list:
        if operation.get('state') == 'EXECUTED' and 'date' in operation:
            unsorted_list.append(operation)
    sort_list = sorted(unsorted_list, key=lambda x: x['date'], reverse=False)
    return sort_list[-5:]


def ch_date(list):
    """
    приведение и замена даты к формату ДД.ММ.ГГГГ
    """
    for operation in list:
        date = operation['date']
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f').date()
        date_fix = ("{}.{}.{}".format(date_obj.day, date_obj.month, date_obj.year))
        operation['date'] = date_fix
    return list


def hide_info(list):
    """
    замена значений данных счетов на скрытые
    """
    for operation in list:
        if 'from' in operation:
            info = operation['from'].split()[-1]
            if len(operation['from'].split()[-1]) == 20:
                operation['from'] = 'Cчет **'+info[-4:]
                operation['to'] = 'Cчет **'+info[-4:]
            elif len(operation['from'].split()[-1]) == 16:
                operation['from'] = info[0:6]+'**-****-'+info[12:16]
                operation['to'] = 'Cчет **' + info[-4:]
        else:
            info = operation['to'].split()[-1]
            operation['from'] = ''
            operation['to'] = 'Cчет **' + info[-4:]
    return list


def get_info(final_list):
    """
    обозначение переменных для вывода -> вывод информации
    """
    for operation in final_list:
        date = operation['date']; description = operation['description']
        frm = operation['from']; to = operation['to']; summ = operation['operationAmount']['amount']
        print(f'{date} {description}\n{frm} -> {to}\n{summ} руб.\n')


def main():
    a = hide_info(ch_date(sort_list(get_list())))
    get_info(a)
