from typing import List


def my_func(coord: List[int], d: int, vertexes: dict) -> int:
    """
    Функция которая вычисляет расположение точки относительно треугольника.

    :param coord: координаты точки
    :type coord: List[int]
    :param d: величина равных сторон равнобедренного треугольника
    :type d: int
    :param vertexes: словарь координат вершин треугольника
    :type vertexes: dict

    :return: числовое значение положения точки относительно треугольника
    :rtype: int
    """
    if (d - coord[0]) >= coord[1] >= 0 and coord[0] >= 0:
        return 0

    min_val = float('inf')
    min_vertex_num = None

    for vertex_num, value in vertexes.items():
        local_min = ((value[0] - coord[0]) ** 2 + (value[1] - coord[1]) ** 2) ** 0.5
        if local_min < min_val:
            min_val = local_min
            min_vertex_num = vertex_num

    return min_vertex_num


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    d = int(input())
    coord = list(map(int, input().split()))

    vertexes = {
        1: (0, 0),
        2: (d, 0),
        3: (0, d),
    }
    print(my_func(coord, d, vertexes))


if __name__ == '__main__':
    main()
