from typing import List


def get_segment_length(count_segment: int, points: List[int]) -> int:
    """
    Функция которая вычисляет минимальную длину сегмента.

    :param count_segment: количество сегментов
    :type count_segment: int
    :param points: список точек
    :type points: List[int]

    :return: минимальная длина сегмента
    :rtype: int
    """
    left = 0
    right = points[-1] - points[0]
    while left < right:
        length = (right + left) // 2
        cur_count_segment = 0
        max_right = points[0] - 1
        for point in points:
            if point > max_right:
                cur_count_segment += 1
                max_right = point + length
        if cur_count_segment <= count_segment:
            right = length
        else:
            left = length + 1

    return left


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    count_points, count_segment = map(int, input().split())
    points = list(map(int, input().split()))
    points.sort()

    print(get_segment_length(count_segment, points))


if __name__ == '__main__':
    main()
