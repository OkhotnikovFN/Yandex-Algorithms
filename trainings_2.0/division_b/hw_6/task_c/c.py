def f(a: int, b: int, c: int, d: int, x: int) -> int:
    """
    Вычисление значения кубического уравнения.

    :param a: параметр уравнения
    :param a: int
    :param b: параметр уравнения
    :param b: int
    :param c: параметр уравнения
    :param c: int
    :param d: параметр уравнения
    :param d: int
    :param x: вероятный корень уравнения
    :param x: int

    :return: значение уравнения
    :rtype: int
    """
    return a * x ** 3 + b * x ** 2 + c * x + d


def get_root(a: int, b: int, c: int, d: int, eps: float) -> float:
    """
    Функция которая вычисляет корень кубического уравнения.

    :param a: параметр уравнения
    :param a: int
    :param b: параметр уравнения
    :param b: int
    :param c: параметр уравнения
    :param c: int
    :param d: параметр уравнения
    :param d: int
    :param eps: точность, с которой необходимо вычислить корень уравнения
    :param eps: float

    :return: корень кубического уравнения с точностью eps
    :rtype: int
    """
    left = -2000
    right = 2000
    while right - left > eps:
        middle = (left + right) / 2
        if f(a, b, c, d, middle) > 0:
            right = middle
        else:
            left = middle
    return (left + right) / 2


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    A, B, C, D = map(int, input().split())
    EPS = 0.000001
    if A < 0:
        A = -A
        B = -B
        C = -C
        D = -D

    print(get_root(A, B, C, D, EPS))


if __name__ == '__main__':
    main()
