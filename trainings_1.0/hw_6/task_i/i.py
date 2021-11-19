from typing import List, Callable, Tuple


def check(inconvenience: int, params: Tuple[int, int, List[int]]) -> bool:
    """
    Функция которая вычисляет наименьшее возможное значение максимального числа неудобства сформированных бригад.
        Параметры:
            :param inconvenience: предполагаемое число неудобства
            :type inconvenience: int
            :param params: Tuple с параметрами из условия задачи
            (количество бригад, количество человек в бригаде, список ростов людей)
            :type params: Tuple[int, int, List[int]
        Возвращаемое значение:
            :return: проверяет возможное число неудобства в бригаде inconvenience
            возвращает True, если количество бригад получилось больше или равно требуемому
            :rtype: bool
    """
    required_brigades_count, hum_per_brig, heights = params
    i = 0
    brigades = 0
    while i < len(heights) - hum_per_brig + 1:
        if heights[i + hum_per_brig - 1] - heights[i] <= inconvenience:
            brigades += 1
            i += hum_per_brig
        else:
            i += 1
    return brigades >= required_brigades_count


def left_bin_search(left: int, right: int, check_func: Callable, params: Tuple[int, int, List[int]]) -> int:
    """
    Функция которая вычисляет наименьшее возможное значение максимального числа неудобства сформированных бригад.
        Параметры:
            :param left: минимальное возможное значение числа неудобства
            :type left: int
            :param right: максимальное возможное значение числа неудобства 
            :type right: int
            :param check_func: функция проверки условия в бинарном поиске
            :type check_func: Callable
            :param params: Tuple с параметрами из условия задачи
            (количество бригад, количество человек в бригаде, список ростов людей)
            :type params: Tuple[int, int, List[int]
        Возвращаемое значение:
            :return: наименьшее возможное значение максимального числа неудобства
            :rtype: int
    """
    while left < right:
        middle = (left + right) // 2
        if check_func(middle, params):
            right = middle
        else:
            left = middle + 1
    return left


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, r, c = tuple(map(int, input().split()))
    heights = sorted([int(input()) for _ in range(n)])
    print(left_bin_search(0, heights[-1] - heights[0], check, (r, c, heights)))


if __name__ == '__main__':
    main()
