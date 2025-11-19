import csv
from tabulate import tabulate
from collections import defaultdict
import argparse


def load_table(table):
    with open(table, mode='r') as file:
        csv_reader = csv.reader(file)
        lst = []
        for row in csv_reader:
            lst.append(row)
    return lst


def func1(data):
    lst = []
    for item in data:
        lst.append((item[1], item[3]))
    return lst


def func2(data):
    data = data[1:]
    positions_dict = defaultdict(list)
    for position, performance in data:
        positions_dict[position].append(float(performance))
    result = [(pos, round(sum(scores) / len(scores), 1)) for pos, scores in positions_dict.items()]
    sorted_lst = sorted(result, key=lambda x: x[1], reverse=True)
    return sorted_lst


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Скрипт для анализа сотрудников.")
    parser.add_argument("--files", nargs="+", help="Файлы CSV для загрузки")
    parser.add_argument("--report", choices=["performance"], default="performance", help="Тип генерируемого отчета")
    args = parser.parse_args()
    try:
        # Загружаем таблицы из указанных файлов
        tables = [load_table(f) for f in args.files]

        # Объединяем данные из таблиц
        combined_data = []
        for t in tables:
            extracted_data = func1(t)
            combined_data.extend(extracted_data[1:])

        # Генерируем итоговую таблицу
        final_data = func2(combined_data)

        # Выводим итоговую таблицу
        headers = ["Position", "Performance"]
        print(tabulate(final_data, headers=headers, tablefmt="fancy_grid"))
    except Exception as e:
        print(e)
