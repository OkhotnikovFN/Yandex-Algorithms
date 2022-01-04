from typing import List


def find_max_sum(input_array: List[int]) -> int:
    """
    Функция которая вычисляет максимальную сумму на отрезке в данном массиве.

    :param input_array: входной массив
    :type input_array: List[int]

    :return: максимальная сумма
    :rtype: int
    """
    prefix_sum = []
    prev = 0

    for num in input_array:
        prev += num
        if prev < 0:
            prev = 0
        else:
            prefix_sum.append(prev)

    if not prefix_sum:
        return max(input_array)
    else:
        return max(prefix_sum)


def main():
    """Основная функция для чтения входных данных и вывода результата."""

    n = int(input())
    input_array = list(map(int, input().split()))
    print(find_max_sum(input_array))


if __name__ == '__main__':
    main()
