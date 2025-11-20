import pytest

from main import load_table, func1, func2


def test_load_table():
    result = load_table('employees1.csv')
    assert isinstance(result, list)


def test_load_table_incorrect_filename():
    incorrect_filename = 'non_existent_file.csv'
    with pytest.raises(FileNotFoundError):
        load_table(incorrect_filename)


def test_basic_case_func1():
    data = [(1, 'a', 3, 'b'), (4, 'c', 6, 'd')]
    expected = [('a', 'b'), ('c', 'd')]
    result = func1(data)
    assert result == expected


def test_empty_input_func1():
    data = []
    expected = []
    result = func1(data)
    assert result == expected


def test_invalid_input_func1():
    data = [(1, 'a'), (2, 'b', 3)]  # Not enough elements
    with pytest.raises(IndexError):
        func1(data)


def test_basic_case_func2():
    data = [
        ['Position', 'Performance'],
        ['Dev', '3.5'],
        ['Dev', '4.0'],
        ['QA', '2.5'],
        ['QA', '3.0']
    ]
    expected = [('Dev', 3.8), ('QA', 2.8)]
    assert func2(data) == expected


def test_invalid_performance_score_func2():
    data = [
        ['Position', 'Performance'],
        ['Dev', '3.5'],
        ['Dev', '4.0'],
        ['QA', 'invalid_param'],
        ['QA', '3.0']
    ]
    with pytest.raises(ValueError):
        func2(data)

