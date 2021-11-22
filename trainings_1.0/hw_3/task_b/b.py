from typing import List


def get_count_uniq_numbers(input_list_1: List[int], input_list_2: List[int]) -> List[int]:
    """
    Функция которая выделяет все числа, которые входят как в первый, так и во второй список входных данных.

    :param input_list_1: список который необходимо проверить
    :type input_list_1: List[int]
    :param input_list_2: список который необходимо проверить
    :type input_list_2: List[int]

    :return: все числа, которые входят как в первый, так и во второй список в порядке возрастания
    :rtype: List[int]
    """
    set_1 = set(input_list_1)
    set_2 = set(input_list_2)
    result = sorted(list(set_1 & set_2))
    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    list_1 = list(map(int, input().split()))
    list_2 = list(map(int, input().split()))
    print(*get_count_uniq_numbers(list_1, list_2))


if __name__ == '__main__':
    main()
