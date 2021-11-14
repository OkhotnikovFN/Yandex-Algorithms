from typing import Tuple, List


def find_numbers(numbers_list: List[int]) -> Tuple[int, int]:
    """
    Функция которая находит в списке два числа, произведение которых максимально.
        Параметры:
            :param numbers_list: исследуемый список чисел
            :type numbers_list: List[int]
        Возвращаемое значение:
            :return: tuple из двух чисел
            :rtype: Tuple[int, int]
    """
    max_plus = 0
    second_plus = 0
    max_minus = 0
    second_minus = 0

    for num in numbers_list:
        if num > 0:
            if num >= max_plus:
                max_plus, second_plus = num, max_plus
            elif num > second_plus:
                second_plus = num
        if num < 0:
            if num <= max_minus:
                max_minus, second_minus = num, max_minus
            elif num < second_minus:
                second_minus = num

    if len(numbers_list) == 2:
        if numbers_list[0] >= numbers_list[1]:
            return numbers_list[1], numbers_list[0]
        else:
            return numbers_list[0], numbers_list[1]
    elif max_plus * second_plus > max_minus * second_minus:
        return second_plus, max_plus
    else:
        return max_minus, second_minus


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    input_list = list(map(int, input().split()))
    print(*find_numbers(input_list))


if __name__ == '__main__':
    main()
