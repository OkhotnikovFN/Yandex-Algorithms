from typing import List, Tuple

LEFT = 1
RIGHT = -1


def get_pointed_length(pointed_segments: List[Tuple[int, int]]) -> int:
    """
    Функция которая вычисляет длину окрашенной части прямой.

    :param pointed_segments: список с точками начала и конца окрашенных сегментов
    :type pointed_segments: List[Tuple[int, int]]

    :return: общая длинна окрашенных сегментов
    :rtype: int
    """
    length = 0
    segments_intersection = 0
    left = None
    right = None
    for segment in pointed_segments:
        segments_intersection += segment[1]
        if left is None and segment[1] == LEFT:
            left = segment[0]
        if segment[1] == RIGHT:
            right = segment[0]
        if segments_intersection == 0:
            length += right - left
            left = None
            right = None

    return length


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())

    pointed_segments = []
    for _ in range(N):
        L, R = map(int, input().split())
        pointed_segments.append((L, LEFT))
        pointed_segments.append((R, RIGHT))
    pointed_segments.sort()

    print(get_pointed_length(pointed_segments))


if __name__ == '__main__':
    main()
