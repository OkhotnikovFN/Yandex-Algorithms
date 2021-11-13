def determine_triangle(a: int, b: int, c: int) -> str:
    """
    Функция определения возможности построения треугольника по трем сторонам.
        Параметры:
            :param a: сторона треугольника
            :type a: int
            :param b: сторона треугольника
            :type b: int
            :param c: сторона треугольника
            :type c: int
        Возвращаемое значение:
            :return: решение о возможности построения треугольника
            :rtype: str
    """
    verdict = 'YES' if a < (b + c) and b < (a + c) and c < (a + b) else 'NO'
    return verdict


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a = int(input())
    b = int(input())
    c = int(input())
    print(determine_triangle(a, b, c))


if __name__ == '__main__':
    main()
