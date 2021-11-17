from collections import defaultdict
from sys import stdin


def define_buyers() -> dict:
    """
    Функция которая определяет список всех покупателей,
    а для каждого покупателя считает количество приобретенных им единиц каждого вида товаров.
        Возвращаемое значение:
            :return: словарь покупателей и товаров, которые они приобрели
            :rtype: dict
    """
    clients = defaultdict(lambda: defaultdict(int))
    for line in stdin.readlines():
        client, thing, value = line.split()
        clients[client][thing] += int(value)

    return clients


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    result = define_buyers()

    for client in sorted(result):
        print(client + ':')
        for thing in sorted(result[client]):
            print(thing, result[client][thing])


if __name__ == '__main__':
    main()
