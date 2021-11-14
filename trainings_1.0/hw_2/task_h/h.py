from typing import Tuple, List


def find_numbers(numbers_list: List[int]) -> Tuple[int, int, int]:
    """
    Функция которая находит в списке три числа, произведение которых максимально.
        Параметры:
            :param numbers_list: исследуемый список чисел
            :type numbers_list: List[int]
        Возвращаемое значение:
            :return: tuple из трех чисел
            :rtype: Tuple[int, int, int]
    """
    max_plus = float('-inf')
    second_plus = float('-inf')
    third_plus = float('-inf')

    max_minus = float('inf')
    second_minus = float('inf')

    for num in numbers_list:
        if num > max_plus:
            max_plus, second_plus, third_plus = num, max_plus, second_plus
        elif num > second_plus:
            second_plus, third_plus = num, second_plus
        elif num > third_plus:
            third_plus = num

        if num < max_minus:
            max_minus, second_minus = num, max_minus
        elif num < second_minus:
            second_minus = num

    if max_plus * second_plus * third_plus >= max_minus * second_minus * max_plus:
        return third_plus, second_plus, max_plus
    else:
        return max_minus, second_minus, max_plus


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    input_list = list(map(int, input().split()))
    print(*find_numbers(input_list))


if __name__ == '__main__':
    main()
