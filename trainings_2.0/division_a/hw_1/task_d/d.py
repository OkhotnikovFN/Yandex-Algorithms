from typing import List, Tuple


def body_swap(swaps_list: List[Tuple[int, int]], bodies: List[int], person_1: int, person_2: int) -> int:
    """
    Функция которая перемещает разум двух людей.

    :param swaps_list: список совершенных перемещений
    :type swaps_list: Tuple[int, int]
    :param bodies: список тел с разумами
    :type bodies: List[int]
    :param person_1: первый человек
    :type person_1: int
    :param person_2: второй человек
    :type person_2: int

    :return: разум второго человека
    :rtype: int
    """
    swaps_list.append((person_1, person_2))
    bodies[person_1], bodies[person_2] = bodies[person_2], bodies[person_1]
    return bodies[person_2]


def get_all_swaps(bodies: List[int], n: int) -> List[Tuple[int, int]]:
    """
    Функция которая вычисляет необходимые перемещения.

    :param bodies: список тел с разумами
    :type bodies: List[int]
    :param n: первый человек
    :type n: int

    :return: список совершенных перемещений
    :rtype: List[Tuple[int, int]]
    """
    result = []
    for i in range(1, n - 1):
        if bodies[i] != i:
            now = i
            while bodies[now] != i:
                now = body_swap(result, bodies, now, n - 1)
            now = body_swap(result, bodies, now, n)
            body_swap(result, bodies, now, n)
            body_swap(result, bodies, bodies[n - 1], n - 1)

    if bodies[n - 1] == n:
        body_swap(result, bodies, n - 1, n)

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, m = map(int, input().split())
    bodies = [0] * (n + 1)

    for i in range(1, n + 1):
        bodies[i] = i

    for _ in range(m):
        a, b = map(int, input().split())
        bodies[a], bodies[b] = bodies[b], bodies[a]

    result = get_all_swaps(bodies, n)
    for val in result:
        print(*val)


if __name__ == '__main__':
    main()
