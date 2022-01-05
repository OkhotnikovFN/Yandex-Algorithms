from typing import List


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
    if nums_list[left] >= search_num:
        return left


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
    if nums_list[left] <= search_num:
        return left


def get_nums_count(left: int, right: int, nums_list: List[int], nums_count: int) -> int:
    """
    Функция которая вычисляет количество элементов списка nums_list, которые лежат в границе от left до right.

    :param left: левая граница
    :type left: int
    :param right: правая граница
    :type right: int
    :param nums_list: исследуемый список
    :type nums_list: List[int]
    :param nums_count: количество элементов в списке
    :type nums_count: int

    :return: число элементов, значение которых лежит в границе от left до right
    :rtype: int
    """
    l_index = l_bin_search(0, nums_count - 1, left, nums_list)
    r_index = r_bin_search(0, nums_count - 1, right, nums_list)
    count = 0
    if l_index is not None and r_index is not None:
        count = r_index - l_index + 1

    return count


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())
    list_n = list(map(int, input().split()))
    list_n.sort()
    K = int(input())

    for _ in range(K):
        L, R = map(int, input().split())
        print(get_nums_count(L, R, list_n, N), end=' ')


if __name__ == '__main__':
    main()
