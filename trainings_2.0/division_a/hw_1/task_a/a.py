from typing import Union


def solve_equation(a: int, b: int, c: int, d: int) -> Union[str, int]:
    """
    Функция которая решает уравнение вида ( ax + b ) : ( cx + d ) = 0 в целых числах.

    :param a: параметр уравнения
    :type a: int
    :param b: параметр уравнения
    :type b: int
    :param c: параметр уравнения
    :type c: int
    :param d: параметр уравнения
    :type d: int

    :return: решение если оно есть, INF - если решений бесконечно много, NO - если решений нет
    :rtype: Union[str, int]
    """
    if a == b == 0:
        return 'INF'

    if not b % a and -b / a * c + d != 0:
        return -b // a

    return 'NO'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(solve_equation(a, b, c, d))


if __name__ == '__main__':
    main()
