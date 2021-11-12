def determine_triangle(a, b, c):
    """Функция определения возможности построения треугольника по трем сторонам"""
    coef = (a * a - b * b - c * c) / (2 * b * c)
    return 'YES' if -1 < coef < 1 else 'NO'


def main():
    """Основная функция для чтения входных данных и вывода результата"""
    a = int(input())
    b = int(input())
    c = int(input())
    print(determine_triangle(a, b, c))


if __name__ == '__main__':
    main()
