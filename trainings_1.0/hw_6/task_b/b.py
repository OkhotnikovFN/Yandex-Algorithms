from typing import List


def bin_search(number: int, input_list: List[int], length_input_list: int) -> int:
    """
    Функция левого бинарного поиска ближайшего к number числа в последовательности.

    :param input_list: отсортированный список с числами
    :type input_list: List[int]
    :param number: искомое число
    :type number: int
    :param length_input_list: длинна input_list
    :type length_input_list: int

    :return: ближайшее число в списке к искомому
    :rtype: int
    """
    left = 0
    right = length_input_list - 1
    while left < right:
        middle = (left + right) // 2
        if number <= input_list[middle]:
            right = middle
        elif number > input_list[middle]:
            left = middle + 1

    if left == 0 or abs(input_list[left] - number) < abs(input_list[left - 1] - number):
        return input_list[left]
    else:
        return input_list[left - 1]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, k = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_k = map(int, input().split())
    for k_item in list_k:
        print(bin_search(k_item, list_n, n))


if __name__ == '__main__':
    main()
