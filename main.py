import csv
from tabulate import tabulate
from collections import defaultdict



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
    data1 = load_table('employees1.csv')
    data2 = load_table('employees2.csv')
    extracted_data1 = func1(data1)
    extracted_data2 = func1(data2)
    general_list = extracted_data1 + extracted_data2[1:]
    final_data = func2(general_list)
    headers = ["position", "performance"]
    print(tabulate(final_data, headers=headers, tablefmt='fancy_grid'))
