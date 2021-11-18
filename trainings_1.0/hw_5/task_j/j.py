from collections import defaultdict
from typing import List, Tuple


def get_squared_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """
    Функция определяет квадрат расстояния между точками.
        Параметры:
            :param a: координаты первой точки
            :type a: Tuple[int, int]
            :param b: координаты второй точки
            :type b: Tuple[int, int]
        Возвращаемое значение:
            :return: квадрат расстояния между точками
            :rtype: int
    """
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def get_triangles_count(points: List[Tuple[int, int]]) -> int:
    """
    Функция определяет количество равнобедренных треугольников.
        Параметры:
            :param points: список координат точек
            :type points: List[Tuple[int, int]
        Возвращаемое значение:
            :return: количество равнобедренных треугольников
            :rtype: int
    """
    triangles_count = 0
    for first_index, first_point in enumerate(points):
        points_by_distances = defaultdict(list)
        for second_index, second_point in enumerate(points):
            if first_index == second_index:
                continue

            squared_distance = get_squared_distance(first_point, second_point)

            for previous_point in points_by_distances[squared_distance]:
                if 4 * squared_distance > get_squared_distance(previous_point, second_point):
                    triangles_count += 1

            points_by_distances[squared_distance].append(second_point)

    return triangles_count


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(get_triangles_count(points))


if __name__ == '__main__':
    main()
