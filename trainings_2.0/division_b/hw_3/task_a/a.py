from typing import List


def get_nums_count(first_list: List[str], second_list: List[str]) -> int:
    """
    Функция которая определяет количество чисел, которые находятся как в первом так и во втором списках.

    :param first_list: первый список
    :type first_list: List[str]
    :param second_list: второй список
    :type second_list: List[str]

    :return: количество совпадающих чисел
    :rtype: int
    """

    return len(set(first_list) & set(second_list))


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    first_list = input().split()
    second_list = input().split()
    print(get_nums_count(first_list, second_list))


if __name__ == '__main__':
    main()
