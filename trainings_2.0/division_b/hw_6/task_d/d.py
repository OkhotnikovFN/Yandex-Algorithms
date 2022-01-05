def cut_tree(rest_1: int, rest_2: int, count_1: int, count_2: int, days_count: int) -> int:
    """
    Функция которая вычисляет количество срубленных деревьев за days_count дней.

    :param rest_1: периодичность отдыха первого лесоруба
    :type rest_1: int
    :param rest_2: периодичность отдыха второго лесоруба
    :type rest_2: int
    :param count_1: количество деревьев, которые срубает первый лесоруб за день
    :type count_1: int
    :param count_2: количество деревьев, которые срубает второй лесоруб за день
    :type count_2: int
    :param days_count: предполагаемое количество дней
    :type days_count: int

    :return: количество срубленных деревьев
    :rtype: int
    """
    rest_days_1 = days_count // rest_1
    rest_days_2 = days_count // rest_2
    result = (days_count - rest_days_1) * count_1 + (days_count - rest_days_2) * count_2

    return result


def get_days(trees_count: int, rest_1: int, rest_2: int, count_1: int, count_2: int) -> int:
    """
    Функция которая вычисляет необходимое количество дней, чтобы лесорубы отчислили поле от деревьев.

    :param trees_count: общее количество деревьев
    :type trees_count: int
    :param rest_1: периодичность отдыха первого лесоруба
    :type rest_1: int
    :param rest_2: периодичность отдыха второго лесоруба
    :type rest_2: int
    :param count_1: количество деревьев, которые срубает первый лесоруб за день
    :type count_1: int
    :param count_2: количество деревьев, которые срубает второй лесоруб за день
    :type count_2: int

    :return: необходимое количество дней
    :rtype: int
    """
    left = trees_count // (count_1 + count_2)
    right = trees_count
    while left < right:
        middle = (left + right) // 2
        if cut_tree(rest_1, rest_2, count_1, count_2, middle) >= trees_count:
            right = middle
        else:
            left = middle + 1
    return left


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    count_1, rest_1, count_2, rest_2, X = map(int, input().split())
    print(get_days(X, rest_1, rest_2, count_1, count_2))


if __name__ == '__main__':
    main()
