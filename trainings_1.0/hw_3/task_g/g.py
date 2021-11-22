def get_count_turtles(n: int) -> int:
    """
    Функция которая проверяет количество черепах, которые говорят правду.

    :param n: количество черепах
    :type n: int

    :return: количество черепах, которые говорят правду
    :rtype: int
    """

    turtles_indications = set()

    for i in range(n):
        a, b = tuple(map(int, input().split()))
        if 0 <= a <= n - 1 and b == n - 1 - a:
            turtles_indications.add((a, b))

    return len(turtles_indications)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    print(get_count_turtles(n))


if __name__ == '__main__':
    main()
