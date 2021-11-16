def get_count_shots(n: int) -> int:
    """
    Функция которая вычисляет минимальное количество выстрелов, чтобы сбить всех птиц.
        Параметры:
            :param n: количество птиц, которых необходимо сбить
            :type n: int
        Возвращаемое значение:
            :return: количество выстрелов
            :rtype: int
    """
    bird_coord = set()

    for i in range(n):
        x, y = tuple(map(int, input().split()))
        bird_coord.add(x)

    return len(bird_coord)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    print(get_count_shots(n))


if __name__ == '__main__':
    main()
