from typing import List, Set


def get_possible_car_numbers(sets_list: List[Set[str]]) -> List[str]:
    """
    Функция которая определяет номера автомобилей, согласующиеся с максимальным количеством свидетелей.

    :param sets_list: список множеств с символами, которые могли быть в номере
    :type sets_list: List[Set[str]]

    :return: список с возможными номерами
    :rtype: List[str]
    """
    n = int(input())

    numbers_dict = {}
    for x in range(n):
        number = input()
        number_set = set([char for char in number])
        count = 0
        for single_set in sets_list:
            if single_set.issubset(number_set):
                count += 1
        if count in numbers_dict:
            numbers_dict[count].append(number)
        else:
            numbers_dict[count] = [number]

    return numbers_dict[max(numbers_dict)]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    m = int(input())

    sets_list = []
    for x in range(m):
        sets_list.append(set([char for char in input()]))
    print(*get_possible_car_numbers(sets_list), sep='\n')


if __name__ == '__main__':
    main()
