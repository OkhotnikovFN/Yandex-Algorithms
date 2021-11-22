from typing import List


def apps_per_floor(m: int, k: int, p: int, n: int) -> List[int]:
    """
    Функция которая определяет возможное количество квартир на этаже в доме.

    :param m: количество этажей в доме
    :type m: int
    :param k: номер квартиры
    :type k: int
    :param p: номер подъезда
    :type p: int
    :param n: номер этажа
    :type n: int

    :return: список с возможным количеством квартир на этаже
    :rtype: List[int]
    """
    min_bound = k // (m * (p - 1) + n)
    max_bound = (k - 1) // (m * (p - 1) + n - 1)
    possible_qs = []
    for q in range(min_bound, max_bound + 1):
        if q != 0 and (m * (p - 1) + n - 1) * q + (k - 1) % q == k - 1:
            possible_qs.append(q)

    return possible_qs


def define_parameters(k1: int, m: int, k2: int, p2: int, n2: int) -> List[int]:
    """
    Функция которая определяет этаж и подъезд первой квартиры, если это возможно.
        Параметры:
            :param k1: номер квартиры 1
            :type k1: int
            :param m: количество этажей в доме
            :type m: int
            :param k2: номер квартиры 2
            :type k2: int
            :param p2: номер подъезда  квартиры 2
            :type p2: int
            :param n2: номер этажа  квартиры 2
            :type n2: int
        Возвращаемое значение:
            :return: список из двух значений, первое - подъезд квартиры, второе - этаж квартиры
            :rtype: List[int]
    """
    if not (0 <= n2 <= m):
        return [-1, -1]

    if p2 == 1 and n2 == 1:
        if k1 <= k2:
            return [1, 1]
        else:
            possible_qs = range(k2, k1 + 1)
    else:
        possible_qs = apps_per_floor(m, k2, p2, n2)

    result = [-1, -1]
    for q in possible_qs:
        floor_index = ((k1 - 1 - (k1 - 1) % q) / q) + 1
        n1 = floor_index % m
        p1 = ((floor_index - n1) / m) + 1

        if n1 == 0:
            n1 = m
            p1 -= 1
        if result == [-1, -1]:
            result = [p1, n1]
        else:

            if p1 != result[0]:
                result[0] = 0
            if n1 != result[1]:
                result[1] = 0

    return list(map(int, result))


def main():
    """
    Основная функция для чтения входных данных и вывода результата.
        K1 - номер квартиры 1
        M - количество этажей в доме
        K2 - номер квартиры 2
        P2 - подъезд квартиры 2
        P3 - этаж квартиры 2
    """
    K1, M, K2, P2, N2 = map(lambda x: int(x), input().split())
    print(*define_parameters(K1, M, K2, P2, N2))


if __name__ == '__main__':
    main()
