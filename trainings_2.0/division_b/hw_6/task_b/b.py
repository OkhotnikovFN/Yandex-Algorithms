from typing import List, Tuple


def l_bin_search(left: int, right: int, search_num: int, nums_list: List[int]) -> int:
    """
    Левый бинарный поиск.

    :param left: левая гранца
    :type left: int
    :param right: правая граница
    :type right: int
    :param search_num: искомое число
    :type search_num: int
    :param nums_list: исследуемый список
    :type nums_list: List[int]

    :return: индекс искомого числа
    :rtype: int
    """
    while left < right:
        m = (left + right) // 2
        if nums_list[m] >= search_num:
            right = m
        else:
            left = m + 1
    if nums_list[left] == search_num:
        return left + 1


def r_bin_search(left, right, search_num, nums_list: List[int]) -> int:
    """
    Правый бинарный поиск.

    :param left: левая гранца
    :type left: int
    :param right: правая граница
    :type right: int
    :param search_num: искомое число
    :type search_num: int
    :param nums_list: исследуемый список
    :type nums_list: int

    :return: индекс искомого числа
    :rtype: int
    """
    while left < right:
        m = (left + right + 1) // 2
        if nums_list[m] <= search_num:
            left = m
        else:
            right = m - 1
    if nums_list[left] == search_num:
        return left + 1


def get_borders(desired_number: int, nums_list: List[int], nums_count: int) -> Tuple[int, int]:
    """
    Функция которая определяет в заданном массиве номер самого левого и самого правого элемента, равного искомому числу.

    :param desired_number: искомое число
    :type desired_number: int
    :param nums_list: исследуемый список
    :type nums_list: List[int]
    :param nums_count: количество элементов в списке
    :type nums_count: int

    :return: значение левого и правого индексов, если они существуют
    :rtype: Tuple[int, int]
    """
    left_index = l_bin_search(0, nums_count - 1, desired_number, nums_list)
    right_index = r_bin_search(0, nums_count - 1, desired_number, nums_list)
    if left_index is None or right_index is None:
        return 0, 0
    else:
        return left_index, right_index


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())
    list_n = list(map(int, input().split()))
    M = int(input())
    list_m = list(map(int, input().split()))

    for val in list_m:
        print(*get_borders(val, list_n, N))


if __name__ == '__main__':
    main()
