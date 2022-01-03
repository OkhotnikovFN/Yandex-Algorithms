def get_count_max_nums() -> int:
    """
    Функция которая определят, сколько элементов последовательности равны ее наибольшему элементу.

    :return: количество элементов равных наибольшему элементу последовательности
    :rtype: int
    """
    counter = 0
    max_num = digit = int(input())

    while digit:
        if digit > max_num:
            counter = 1
            max_num = digit
        elif digit == max_num:
            counter += 1

        digit = int(input())

    return counter


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    print(get_count_max_nums())


if __name__ == '__main__':
    main()
