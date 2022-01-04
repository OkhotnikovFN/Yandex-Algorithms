from typing import List, Iterator


def get_array_prefix_sum(input_array: Iterator[int]) -> List[int]:
    """
    Функция которая, вычисляет массив префиксных сумм.

    :param input_array: массив чисел
    :type input_array: Iterator[int]

    :return: массив префиксных сумм
    :rtype: List[int]
    """
    prefix_sum = [0]
    prev = 0

    for num in input_array:
        prev += num
        prefix_sum.append(prev)

    return prefix_sum


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, q = map(int, input().split())
    input_array = map(int, input().split())

    prefix_sum = get_array_prefix_sum(input_array)
    for _ in range(q):
        start, end = map(int, input().split())
        print(prefix_sum[end] - prefix_sum[start - 1])


if __name__ == '__main__':
    main()
