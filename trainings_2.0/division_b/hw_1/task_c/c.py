def check_unambiguity_date(x: int, y: int) -> int:
    """
    Функция которая проверяет возможно ли однозначно определить дату.

    :param x: значение месяца или числа
    :type x: int
    :param y: значение месяца или числа
    :type y: int

    :return: 1 - если можно, 0 - если нельзя
    :rtype: int
    """
    if x == y:
        return 1
    if x <= 12 and y <= 12:
        return 0
    return 1


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    x, y, z = map(int, input().split())
    print(check_unambiguity_date(x, y))


if __name__ == '__main__':
    main()
