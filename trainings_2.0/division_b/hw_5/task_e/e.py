from typing import List, Set, Tuple


def find_seq(list_a: List[Tuple[int, int]], list_b: List[Tuple[int, int]],
             list_c: List[int], set_c: Set[int], num: int) -> List[int]:
    """
    Функция которая определяет индексы из массивов list_a, list_b, list_c, такие,
    что сумма элементов с этими индексами равна числу num.

    :param list_a: первый список элементов, с номерами индексов этих элементов
    :type list_a: List[Tuple[int, int]]
    :param list_b: второй  список элементов, с номерами индексов этих элементов
    :type list_b: List[Tuple[int, int]]
    :param list_c: третий  список элементов
    :type list_c: List[int]
    :param set_c: множество элементов третьего массива
    :type set_c: Set[int]
    :param num: проверяемое число
    :type num: int


    :return:
    :rtype:
    """
    array_with_results = []
    for i_a, a in list_a:
        for i_b, b in list_b:
            c = num - a - b
            if c <= 0:
                break
            if c in set_c:
                array_with_results.append((i_a, i_b, list_c.index(c)))
    array_with_results.sort()

    return array_with_results[0] if array_with_results else [-1]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    S = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    source_A = A[1:]
    source_B = B[1:]
    source_C = C[1:]

    A_set = set(source_A)
    A_list = []
    for val in A_set:
        if val < S:
            A_list.append((source_A.index(val), val))
    A_list.sort()

    B_set = set(source_B)
    B_list = []
    for val in B_set:
        if val < S:
            B_list.append((source_B.index(val), val))
    B_list.sort(key=lambda x: x[1])

    C_set = set(source_C)
    print(*find_seq(A_list, B_list, source_C, C_set, S))


if __name__ == '__main__':
    main()
