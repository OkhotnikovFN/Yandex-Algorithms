from functools import reduce
import operator
import math
from typing import List, Tuple


def get_points_tuples(points: List[int]) -> List[Tuple[int, int]]:
    """
    Функция которая формирует координаты.

    :param points: список координат точек
    :type points: List[int]

    :return: Список кортежей с координатами
    :rtype: List[Tuple[int, int]]
    """
    points_coord = []
    for index in range(0, len(points), 2):
        points_coord.append((points[index], points[index + 1]))
    return points_coord


def check_points(points: List[int]) -> bool:
    """
    Функция которая вычисляет являются ли точки вершинами параллелограмма.

    :param points: список координат точек
    :type points: List[int]

    :return: ответ в виде булева значения
    :rtype: bool
    """
    coord_point = get_points_tuples(points)
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coord_point), [len(coord_point)] * 2))
    sorted_points = sorted(coord_point, key=lambda coord: (-135 - math.degrees(
        math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)

    x_side_1 = (sorted_points[0][0] - sorted_points[1][0]) ** 2 + (sorted_points[0][1] - sorted_points[1][1]) ** 2
    x_side_2 = (sorted_points[2][0] - sorted_points[3][0]) ** 2 + (sorted_points[2][1] - sorted_points[3][1]) ** 2
    y_side_1 = (sorted_points[0][0] - sorted_points[3][0]) ** 2 + (sorted_points[0][1] - sorted_points[3][1]) ** 2
    y_side_2 = (sorted_points[2][0] - sorted_points[1][0]) ** 2 + (sorted_points[2][1] - sorted_points[1][1]) ** 2

    return x_side_1 == x_side_2 and y_side_1 == y_side_2


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())
    for i in range(N):
        result_points = list(map(int, input().split()))
        result = check_points(result_points)
        if result:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
