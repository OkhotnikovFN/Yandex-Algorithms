def define_max_high(n: int) -> int:
    """
    Функция которая определяет максимально возможную высоту пирамиды.
        Параметры:
            :param n: количество блоков
            :type n: int
        Возвращаемое значение:
            :return: максимально возможная высота пирамиды
            :rtype: int
    """
    dict_of_blocks = {}
    for _ in range(n):
        w, h = map(int, input().split())
        if w in dict_of_blocks:
            if h > dict_of_blocks[w]:
                dict_of_blocks[w] = h
        else:
            dict_of_blocks[w] = h

    max_height = 0
    for h in dict_of_blocks.values():
        max_height += h

    return max_height


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    print(define_max_high(n))


if __name__ == '__main__':
    main()
