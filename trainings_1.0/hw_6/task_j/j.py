from typing import List


def merge_seq(seq_1: List[int], seq_2: List[int], seq_length) -> int:
    """
    Функция вычисляет левую медиану объединения последовательностей seq_1 и seq_2.

    :param seq_1: отсортированный список с числами
    :type seq_1: List[int]
    :param seq_2: отсортированный список с числами
    :type seq_2: List[int]
    :param seq_length: длинна последовательностей
    :type seq_length: int

    :return: медиана объединения последовательностей
    :rtype: int
    """
    i_1, i_2 = 0, 0
    counter = 0
    while counter < seq_length:
        if seq_1[i_1] >= seq_2[i_2]:
            i_2 += 1
            flag_1 = False
        else:
            i_1 += 1
            flag_1 = True
        counter += 1
    return seq_1[i_1 - 1] if flag_1 else seq_2[i_2 - 1]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, l = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split())))

    for j1 in range(n):
        for j2 in range(j1 + 1, n):
            print(merge_seq(seq[j1], seq[j2], l))


if __name__ == '__main__':
    main()
