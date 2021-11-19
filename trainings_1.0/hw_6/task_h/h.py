from typing import Callable, List


def get_piece_of_wire_count(wires: List[int], required_wires_count: int, check_func: Callable) -> int:
    """
    Функция которая определяет максимальную длину кусков проводов.
        Параметры:
            :param wires: список с длинами исходных проводов
            :type wires: List[int]
            :param required_wires_count: необходимое количество проводов
            :type required_wires_count: int
            :param check_func: функция проверки условия в бинарном поиске
            :type check_func: Callable
        Возвращаемое значение:
            :return: максимальная длина отрезков
            :rtype: int
    """
    left, right = 0, max(wires)
    while left < right:
        middle = (left + right + 1) // 2
        if check_func(middle, wires, required_wires_count):
            left = middle
        else:
            right = middle - 1

    return left


def check(length: int, wires: List[int], required_wires_count: int) -> bool:
    """
    Функция проверки условия в бинарном поиске
        Параметры:
            :param length: предполагаемая длинна кусков провода
            :type length: int
            :param wires: список с длинами исходных проводов
            :type wires: List[int]
            :param required_wires_count: необходимое количество проводов
            :type required_wires_count: int
        Возвращаемое значение:
            :return: проверяет предполагаемую длину кусков проводов length,
            возвращает True, если количество проводов такой длинны больше или равно требуемому required_wires_count
            :rtype: bool
    """
    count = 0
    for rope in wires:
        count += rope // length
    return count >= required_wires_count


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, k = map(int, input().split())
    wires = []
    for _ in range(n):
        wires.append(int(input()))

    print(get_piece_of_wire_count(wires, k, check))


if __name__ == '__main__':
    main()
