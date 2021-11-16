from typing import Set, List, Union


def get_count_uniq_numbers(set_1: Set[int], set_2: Set[int]) -> List[Union[int, str]]:
    """
    Функция которая сравнивает два множества.
    Выводит количество и отсортированные по возрастанию числа, которые есть в обоих множествах,
    количество и отсортированные по возрастанию оставшиеся числа в первом множестве,
    количество и отсортированные по возрастанию оставшиеся числа во втором множестве.
        Параметры:
            :param set_1: первое множество чисел
            :type set_1: Set[int]
            :param set_2: второе множество чисел
            :type set_2: Set[int]
        Возвращаемое значение:
            :return: количество и строковое представление чисел, которые есть в обоих множествах,
                     количество и строковое представление оставшихся чисел в первом множестве,
                     количество и строковое представление оставшихся чисел числа во втором множестве
            :rtype: List[Union[int, str]]
    """
    collective_list = sorted(list(set_1 & set_2))
    collective_str = ' '.join(map(str, collective_list))

    only_1_list = sorted(list(set_1 - set_2))
    only_1_str = ' '.join(map(str, only_1_list))

    only_2_list = sorted(list(set_2 - set_1))
    only_2_str = ' '.join(map(str, only_2_list))

    return [len(collective_list), collective_str, len(only_1_list), only_1_str, len(only_2_list), only_2_str]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, m = map(int, input().split())
    set_n = set()
    set_m = set()

    for _ in range(n):
        set_n.add(int(input()))

    for _ in range(m):
        set_m.add(int(input()))

    print(*get_count_uniq_numbers(set_n, set_m), sep='\n')


if __name__ == '__main__':
    main()
