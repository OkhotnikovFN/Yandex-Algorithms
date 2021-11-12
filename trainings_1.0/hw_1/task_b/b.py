def determine_triangle(a: int, b: int, c: int) -> str:
    """
    Функция определения возможности построения треугольника по трем сторонам.
        Параметры:
            a: сторона треугольника
            b: сторона треугольника
            c: сторона треугольника
        Возвращаемое значение:
            verdict(str): решение о возможности построения треугольника
    """
    coef = (a * a - b * b - c * c) / (2 * b * c)
    verdict = 'YES' if -1 < coef < 1 else 'NO'
    return verdict


def main():
    """Основная функция для чтения входных данных и вывода результата"""
    a = int(input())
    b = int(input())
    c = int(input())
    print(determine_triangle(a, b, c))


if __name__ == '__main__':
    main()
