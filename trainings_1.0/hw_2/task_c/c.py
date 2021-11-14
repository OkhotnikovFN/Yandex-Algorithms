from typing import List


def find_nearest_number(checked_array: List[int], checked_number: int) -> int:
    """
    Функция которая находит в списке число, самое близкое по величине к  данному числу.
        Параметры:
            :param checked_array: список с числами
            :type checked_array: List[int]
            :param checked_number: число, с которым необходимо сравнить список
            :type checked_number: int
        Возвращаемое значение:
            :return: значение числа, самого близкого к данному
            :rtype: int
    """
    difference = abs(checked_array[0] - checked_number)
    nearest_number = checked_array[0]

    for number in checked_array:
        if abs(number - checked_number) < difference:
            difference = abs(number - checked_number)
            nearest_number = number

    return nearest_number


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())
    print(find_nearest_number(array, x))


if __name__ == '__main__':
    main()
