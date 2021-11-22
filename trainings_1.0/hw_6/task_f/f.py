def get_min_time(copies_count: int, copy_time_1: int, copy_time_2: int) -> int:
    """
    Функция определения минимального времени, чтобы сделать copies_count копий.

    :param copies_count: количество необходимых копий
    :type copies_count: int
    :param copy_time_1: время копирования 1-ого принтера
    :type copy_time_1: int
    :param copy_time_2: время копирования 2-ого принтера
    :type copy_time_2: int

    :return: минимальное время
    :rtype: int
    """
    left, right = 0, (copies_count - 1) * max(copy_time_1, copy_time_2)
    while left < right:
        middle = (right + left) // 2
        if (middle // copy_time_1 + middle // copy_time_2) >= copies_count - 1:
            right = middle
        else:
            left = middle + 1

    return left + min(copy_time_1, copy_time_2)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, x, y = map(int, input().split())
    print(get_min_time(n, x, y))


if __name__ == '__main__':
    main()
