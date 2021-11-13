def check_brick(a: int, b: int, c: int, d: int, e: int) -> str:
    """
    Функция которая проверяет пролезет ли кирпич в отверстие в стене.
        Параметры:
            :param a: 1-ая сторона кирпича
            :type a: int
            :param b: 2-ая сторона кирпича
            :type b: int
            :param c: 3-ая сторона кирпича
            :type c: int
            :param d: 1-ая сторона отверстия
            :type d: int
            :param e: 2-ая сторона отверстия
            :type e: int
        Возвращаемое значение:
            :return: количество деталей
            :rtype: Union[Tuple[int, int], int]
    """
    a, b, c = sorted((a, b, c))
    d, e = sorted((d, e))

    return 'YES' if a <= d and b <= e else 'NO'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(check_brick(a, b, c, d, e))


if __name__ == '__main__':
    main()
