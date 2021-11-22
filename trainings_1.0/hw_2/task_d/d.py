from typing import List


def check_array(checked_array: List[int]) -> int:
    """
    Функция которая определяет, сколько в списке элементов, которые больше двух своих соседей.

    :param checked_array: проверяемый список с числами
    :type checked_array: List[int]

    :return: количество элементов, которые больше двух своих соседей
    :rtype: int
    """
    number_count = 0

    for i in range(1, len(checked_array) - 1):
        if checked_array[i] > checked_array[i - 1] and checked_array[i] > checked_array[i + 1]:
            number_count += 1

    return number_count


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    array = list(map(int, input().split()))
    print(check_array(array))


if __name__ == '__main__':
    main()
