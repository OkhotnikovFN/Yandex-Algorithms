from typing import Union, Tuple


def solve_equation(a: float, b: float, c: float,
                   d: float, e: float, f: float) -> Union[Tuple[int, str], Tuple[int, str, str], int]:
    """
    Функция которая решает линейное уравнение вида:
    ax + by = e
    cx + dy = f.
        Параметры:
            :param a: коэффициент уравнения
            :type a: float
            :param b: коэффициент уравнения
            :type b: float
            :param c: коэффициент уравнения
            :type c: float
            :param d: коэффициент уравнения
            :type d: float
            :param e: коэффициент уравнения
            :type e: float
            :param f: коэффициент уравнения
            :type f: float
        Возвращаемое значение:
            :return: числовой код решения и само решение, если оно существует
            :rtype: Union[Tuple[int, str], Tuple[int, str, str], int]
    """
    x = y = sign = None
    defa = a * d - c * b
    if defa:
        x = d * e / (a * d - c * b) - b * f / (a * d - c * b)
        y = -c * e / (a * d - c * b) + a * f / (a * d - c * b)
        # x=x0, y=y0
        sign = 2
    elif b:
        if a:
            if c:
                if d:
                    if a * f == e * c:
                        # y = kx + b
                        x = -(a / b)
                        y = e / b
                        sign = 1
                    else:
                        # нет решений
                        sign = 0
            else:
                if not d:
                    if f:
                        # нет решений
                        sign = 0
                    else:
                        # y = kx + b
                        x = -(a / b)
                        y = e / b
                        sign = 1
        else:
            y = e / b
            if not c:
                if d:
                    if e * d == f * b:
                        # y = y0 x-любое
                        sign = 4
                    else:
                        # нет решений
                        sign = 0
                else:
                    if f:
                        # нет решений
                        sign = 0
                    else:
                        # y = y0 x-любое
                        sign = 4
    else:
        if a:
            x = e / a
            if not d:
                if c:
                    if e * c == f * a:
                        # x = x0 y-любое
                        sign = 3
                    else:
                        # нет решений
                        sign = 0
                else:
                    if f:
                        # нет решений
                        sign = 0
                    else:
                        # x = x0 y-любое
                        sign = 3
        else:
            if e:
                # нет решений
                sign = 0
            else:
                if c:
                    if d:
                        # y = kx + b
                        x = -(c / d)
                        y = (f / d)
                        sign = 1
                    else:
                        # x = x0 y-любое
                        x = f / c
                        sign = 3
                else:
                    if d:
                        # y = y0 x-любое
                        y = f / d
                        sign = 4
                    else:
                        if f:
                            # нет решений
                            sign = 0
                        else:
                            # любая пара решений
                            sign = 5

    if sign == 0 or sign == 5:
        return sign
    elif sign == 1 or sign == 2:
        return sign, f'{x:.5f}', f'{y:.5f}'
    elif sign == 3:
        return sign, f'{x:.5f}'
    elif sign == 4:
        return sign, f'{y:.5f}'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())

    result = solve_equation(a, b, c, d, e, f)
    if isinstance(result, int):
        print(result)
    else:
        print(*result)


if __name__ == '__main__':
    main()
