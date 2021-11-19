from typing import List


def bin_search(number: int, input_list: List[int], length_input_list: int) -> str:
    """
    Функция бинарного поиска элемента в списке.
        Параметры:
            :param input_list: отсортированный список с числами
            :type input_list: List[int]
            :param number: искомое число
            :type number: int
            :param length_input_list: длинна input_list
            :type length_input_list: int
        Возвращаемое значение:
            :return: строковый ответ, присутствия элемента в списке
            :rtype: str
    """
    left = 0
    right = length_input_list - 1
    while left < right:
        middle = (left + right) // 2
        if number <= input_list[middle]:
            right = middle
        elif number > input_list[middle]:
            left = middle + 1

    if number == input_list[left]:
        return 'YES'
    else:
        return 'NO'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, k = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_n.sort()
    list_k = map(int, input().split())
    for k_item in list_k:
        print(bin_search(k_item, list_n, n))


if __name__ == '__main__':
    main()
