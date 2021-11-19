from typing import List, Callable, Tuple


def gen_seq(length: int, x1, d1, a, c, m) -> List[int]:
    """
    Функция которая генерирует последовательности.
        Параметры:
            :param length: длинна последовательности
            :type length: int
            :param x1: первый элемент последовательности
            :type x1: int
            :param d1: параметр для получения следующего значения последовательности
            :type d1: int
            :param a: параметр для получения следующего значения последовательности
            :type a: int
            :param c: параметр для получения следующего значения последовательности
            :type c: int
            :param m: параметр для получения следующего значения последовательности
            :type m: int
        Возвращаемое значение:
            :return: сгенерированная последовательность
            :rtype: List[int]
    """
    seq = [x1]
    d = d1
    for _ in range(length - 1):
        seq.append(seq[-1] + d)
        d = (a * d + c) % m
    return seq


def left_bin_search(left: int, right: int, check_func: Callable, params: Tuple[List[int], int]) -> int:
    """
    Функция вычисляет индекс первого элемента, который больше или равен числу заданному в параметрах params.
        Параметры:
            :param left: левая граница бинарного поиска
            :type left: int
            :param right: правая граница бинарного поиска
            :type right: int
            :param check_func: функция проверки условия в бинарном поиске
            :type check_func: Callable
            :param params: параметры для проверки условия бинарного поиска
            (список элементов, проверяемое число)
            :type params: Tuple[List[int], int]
        Возвращаемое значение:
            :return: индекс искомого элемента
            :rtype: int
    """
    while left < right:
        m = (left + right) // 2
        if check_func(m, params):
            right = m
        else:
            left = m + 1
    return left


def check_is_greater_or_equal_then(index: int, params: Tuple[List[int], int]) -> bool:
    """
    Функция вычисляет является ли значение последовательности из params с индексом index
    большим или равным значению проверяемого числа из params.
        Параметры:
            :param index: левая граница бинарного поиска
            :type index: int
            :param params: параметры для проверки условия бинарного поиска
            (список элементов, проверяемое число)
            :type params: Tuple[List[int], int]
        Возвращаемое значение:
            :return: возвращает True, если значение из последовательности больше или равно проверяемому числу
            :rtype: bool
    """
    seq, x = params
    return seq[index] >= x


def get_less_count(seq: List[int], x: int) -> int:
    """
    Функция вычисляет количество элементов в последовательности меньше чем заданное число (x).
        Параметры:
            :param seq: последовательность с числами
            :type seq: List[int]
            :param x: заданное число
            :type x: int
        Возвращаемое значение:
            :return: количество элементов меньше чем x
            :rtype: int
    """
    ans = left_bin_search(0, len(seq) - 1, check_is_greater_or_equal_then, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


def get_greater_or_equal_count(seq: List[int], x: int) -> int:
    """
    Функция вычисляет количество элементов в последовательности больше чем заданное число (x).
        Параметры:
            :param seq: последовательность с числами
            :type seq: List[int]
            :param x: заданное число
            :type x: int
        Возвращаемое значение:
            :return: количество элементов больше чем x
            :rtype: int
    """
    return len(seq) - get_less_count(seq, x + 1)


def median_merge(seq_1: List[int], seq_2: List[int]) -> int:
    """
    Функция вычисляет левую медиану объединения последовательностей seq_1 и seq_2.
        Параметры:
            :param seq_1: список с числами
            :type seq_1: List[int]
            :param seq_2: список с числами
            :type seq_2: List[int]
        Возвращаемое значение:
            :return: медиана объединения последовательностей
            :rtype: int
    """
    left = min(seq_1[0], seq_2[0])
    right = max(seq_1[-1], seq_2[-1])
    while left < right:
        middle = (left + right) // 2
        less_count = get_less_count(seq_1, middle) + get_less_count(seq_2, middle)
        greater_count = get_greater_or_equal_count(seq_1, middle) + get_greater_or_equal_count(seq_2, middle)
        if less_count <= len(seq_1) - 1 and greater_count <= len(seq_1):
            return middle
        if greater_count > len(seq_1):
            left = middle + 1
        if less_count > len(seq_1) - 1:
            right = middle - 1
    return left


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, l = map(int, input().split())
    seqs = []
    for i in range(n):
        x1, d1, a, c, m = map(int, input().split())
        seqs.append(gen_seq(l, x1, d1, a, c, m))
    for i in range(n):
        for j in range(i + 1, n):
            print(median_merge(seqs[i], seqs[j]))


if __name__ == '__main__':
    main()
