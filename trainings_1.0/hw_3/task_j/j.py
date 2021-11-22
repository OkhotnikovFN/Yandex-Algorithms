from typing import Tuple, List


def extend(rect: List[int], d) -> List[int]:
    """
    Функция которая расширяет прямоугольник возможных координат бегуна.

    :param rect: текущий прямоугольник координат
    :type rect: int
    :param d: расстояние, на которое увеличивается прямоугольник координат
    :type d: int

    :return: расширенный прямоугольник координат
    :rtype: List[int]
    """
    min_plus, max_plus, min_minus, max_minus = rect
    return [min_plus - d, max_plus + d, min_minus - d, max_minus + d]


def intersect(rect_1: List[int], rect_2: List[int]) -> List[int]:
    """
    Функция которая пересекает два прямоугольника координат.
        Параметры:
            :param rect_1: текущий прямоугольник координат
            :type rect_1: List[int]
            :param rect_2: расстояние, на которое увеличивается прямоугольник координат
            :type rect_2: List[int]
        Возвращаемое значение:
            :return: прямоугольник возможных координат бегуна
            :rtype: List[int]
    """
    ans = [max(rect_1[0], rect_2[0]), min(rect_1[1], rect_2[1]), max(rect_1[2], rect_2[2]), min(rect_1[3], rect_2[3])]
    return ans


def define_coordinates(t: int, d: int, n: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Функция которая определяет возможные координаты.
        Параметры:
            :param t: время между сообщениями от навигатора
            :type t: int
            :param d: Манхэттенское расстояние навигатора
            :type d: int
            :param n: количество сообщений от навигатора
            :type n: int
        Возвращаемое значение:
            :return: количество возможных координат, список этих координат
            :rtype: Tuple[int, List[Tuple[int, int]]]
    """
    pos_rect = [0, 0, 0, 0]
    for _ in range(n):
        pos_rect = extend(pos_rect, t)
        nav_x, nav_y = map(int, input().split())
        nav_rect = extend([nav_x + nav_y, nav_x + nav_y, nav_x - nav_y, nav_x - nav_y], d)
        pos_rect = intersect(pos_rect, nav_rect)

    points = []
    for x_plus_y in range(pos_rect[0], pos_rect[1] + 1):
        for x_minus_y in range(pos_rect[2], pos_rect[3] + 1):
            if (x_plus_y + x_minus_y) % 2 == 0:
                x = (x_plus_y + x_minus_y) // 2
                y = x_plus_y - x
                points.append((x, y))

    return len(points), points


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    t, d, n = map(int, input().split())
    result = define_coordinates(t, d, n)
    print(result[0])
    for point in result[1]:
        print(*point)


if __name__ == '__main__':
    main()
