def get_five_count(two_count: int, three_count: int, four_count: int) -> int:
    """
    Функция определения минимального количество пятерок.

    :param two_count: количество двоек
    :type two_count: int
    :param three_count: количество троек
    :type three_count: int
    :param four_count: количество четверок
    :type four_count: int

    :return: минимальное количество пятерок
    :rtype: int
    """
    left = 0
    right = two_count + three_count + four_count + 1

    while left < right:
        middle = (left + right) // 2
        if (2 * two_count + 3 * three_count + 4 * four_count + 5 * middle) * 10 \
                >= 35 * (two_count + three_count + four_count + middle):
            right = middle
        else:
            left = middle + 1

    return left


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a = int(input())
    b = int(input())
    c = int(input())
    print(get_five_count(a, b, c))


if __name__ == '__main__':
    main()
