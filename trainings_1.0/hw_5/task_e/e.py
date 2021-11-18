from collections import Counter
from typing import Tuple, List


def beautiful_trees(k: int, colors: List[int]) -> Tuple[int, int]:
    """
    Функция которая вычисляет координаты левого и правого концов отрезка минимальной длины, удовлетворяющего условию.
        Параметры:
            :param k: количество сортов деревьев
            :type k: int
            :param colors: исходный список деревьев, в котором необходимо найти подотрезок, удовлетворяющего условию
            :type colors: List[int]
        Возвращаемое значение:
            :return: координаты левого и правого концов отрезка минимальной длины
            :rtype: Tuple[int, int]
    """
    left = 0
    segment_colors = Counter()
    best_segment = [0, len(colors)]

    for right, color in enumerate(colors):
        segment_colors[color] += 1
        if len(segment_colors) == k:
            while segment_colors[colors[left]] > 1:
                segment_colors[colors[left]] -= 1
                left += 1

            if right - left < best_segment[1] - best_segment[0]:
                best_segment = (left, right)

    return best_segment[0] + 1, best_segment[1] + 1


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    print(*beautiful_trees(k, colors))


if __name__ == '__main__':
    main()