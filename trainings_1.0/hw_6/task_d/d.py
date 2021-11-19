from typing import Callable, Tuple


def r_bin_search(left: int, right: int, check_func: Callable, params: Tuple[int, int, int, int, int]) -> int:
    """
    Функция бинарного которая по заданным количеству и размеру модулей, а также размеру поля для их размещения,
    определяет максимальную толщину слоя дополнительной защиты, который можно добавить к каждому модулю.
        Параметры:
            :param left: минимальная толщина защиты
            :type left: int
            :param right: максимальная толщина защиты
            :type right: int
            :param check_func: функция проверки условия в бинарном поиске
            :type check_func: Callable
            :param params: Tuple с параметрами из условия задачи
            (количество модулей, сторона модуля, вторая сторона модуля, размер поля, второй размер поля)
            :type params: Tuple[int, int, int, int, int]
        Возвращаемое значение:
            :return: строковый ответ, присутствия элемента в списке
            :rtype: str
    """
    while left < right:
        middle = (left + right + 1) // 2
        if check_func(middle, params):
            left = middle
        else:
            right = middle - 1
    return left


def check(d: int, params: Tuple[int, int, int, int, int]) -> bool:
    """
    Функция проверки условия в бинарном поиске
        Параметры:
            :param d: проверяемая толщина защиты
            :type d: int
            :param params: Tuple с параметрами из условия задачи
            (количество модулей, сторона модуля, вторая сторона модуля, размер поля, второй размер поля)
            :type params: Tuple[int, int, int, int, int]
        Возвращаемое значение:
            :return: проверяет возможное количество установленных модулей при ширине защиты d,
            возвращает True, если количество возможных модулей больше или равно необходимому количеству модулей
            :rtype: bool
    """
    n, a, b, w, h = params
    return (h // (a + 2 * d)) * (w // (b + 2 * d)) >= n or (w // (a + 2 * d)) * (h // (b + 2 * d)) >= n


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    params = tuple(map(int, input().split()))
    print(r_bin_search(0, max(params[3], params[4]), check, params))


if __name__ == '__main__':
    main()
