from typing import Callable, Tuple


def right_bin_search(left: int, right: int, check_func: Callable, params: Tuple[int, int, int]) -> int:
    """
    Функция определения максимальной ширины дорожки.
        Параметры:
            :param left: минимальная ширина дорожки
            :type left: int
            :param right: максимальная ширина дорожки
            :type right: int
            :param check_func: функция проверки условия в бинарном поиске
            :type check_func: Callable
            :param params: Tuple с параметрами из условия задачи
            (размер поля, размер поля, количество плиток)
            :type params: Tuple[int, int, int]
        Возвращаемое значение:
            :return: максимальная ширина дорожки
            :rtype: int
    """
    while left < right:
        middle = (left + right + 1) // 2
        if check_func(middle, params):
            left = middle
        else:
            right = middle - 1
    return left


def check(width: int, params: Tuple[int, int, int]) -> bool:
    """
    Функция проверки условия в бинарном поиске
        Параметры:
            :param width: предполагаемая ширина дорожки
            :type width: int
            :param params: Tuple с параметрами из условия задачи
            (размер поля, размер поля, количество плиток)
            :type params: Tuple[int, int, int]
        Возвращаемое значение:
            :return: проверяет ширину дорожки width,
            возвращает True, если количество используемой плитки меньше или равно общему количеству плитки
            :rtype: bool
    """
    n, m, t = params
    if 2 * width >= n or 2 * width >= m:
        return False
    return n * m - (n - 2 * width) * (m - 2 * width) <= t


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    m = int(input())
    t = int(input())
    left, right = 0, max(n, m)

    print(right_bin_search(left, right, check, (n, m, t)))


if __name__ == '__main__':
    main()
