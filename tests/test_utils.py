from src.utils import sort_list, ch_date, hide_info


def test_sort_list():
    test_list = [{'state': 'EXECUTED', 'date': '2019-09-29T14:25:28.588059'},
                 {'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051'},
                 {'state': 'CANCELED', 'date': '2019-11-13T17:38:04.800051'},
                 {'state': 'EXECUTED'}]
    assert sort_list(test_list) == [{'state': 'EXECUTED', 'date': '2019-09-29T14:25:28.588059'},
                                    {'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051'}]


def test_sort_list_no_keys():
    test_list = [{'state': 'CANCELED', 'date': '2019-11-13T17:38:04.800051'},
                 {'state': 'EXECUTED'}]
    assert sort_list(test_list) == []

def test_ch_date():
    test_list = [{'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051'}]
    assert ch_date(test_list) == [{'state': 'EXECUTED', 'date': '13.11.2019'}]


def test_hide_info_no_From():
    test_list = [{'to': 'Счет 90424923579946435907'}]
    assert hide_info(test_list)  == [{'to': 'Cчет **5907', 'from': ''}]


def test_hide_16():
    test_list = [{'from': '1111000011110000', 'to': 'Счет 90424923579946435907'}]
    assert hide_info(test_list) == [{'from': '111100**-****-0000', 'to': 'Cчет **0000'}]


def test_hide_20():
    test_list = [{'from': '11110000111100001234', 'to': 'Счет 90424923579946435907'}]
    assert hide_info(test_list) == [{'from': 'Cчет **1234', 'to': 'Cчет **1234'}]