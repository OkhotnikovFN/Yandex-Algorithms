from typing import Tuple


def calc_square(a: int, b: int) -> int:
    """
    Функция которая вычисляет площадь по двум сторонам.
        Параметры:
            :param a: 1-ая сторона
            :type a: int
            :param b: 2-ая сторона
            :type b: int
        Возвращаемое значение:
            :return: площадь
            :rtype: int
    """
    return a * b


def define_min_table_size(a1: int, b1: int, a2: int, b2: int) -> Tuple[int, int]:
    """
    Функция которая вычисляет минимальный размер стола.
        Параметры:
            :param a1: 1-ая сторона 1-ого ноутбука
            :type a1: int
            :param b1: 2-ая сторона 1-ого ноутбука
            :type b1: int
            :param a2: 1-ая сторона 2-ого ноутбука
            :type a2: int
            :param b2: 2-ая сторона 2-ого ноутбука
            :type b2: int
        Возвращаемое значение:
            :return: tuple с размерами стола
            :rtype: Tuple[int, int]
    """
    possible_sizes = [(a1 + a2, max(b1, b2)),
                      (a1 + b2, max(b1, a2)),
                      (b1 + a2, max(a1, b2)),
                      (b1 + b2, max(a1, a2))]

    min_square = calc_square(*possible_sizes[0])
    index = 0

    for i, possible_size in enumerate(possible_sizes):
        possible_square = calc_square(*possible_size)
        if possible_square < min_square:
            min_square = possible_square
            index = i

    return possible_sizes[index]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a1, b1, a2, b2 = map(int, input().split())
    print(*define_min_table_size(a1, b1, a2, b2))


if __name__ == '__main__':
    main()
