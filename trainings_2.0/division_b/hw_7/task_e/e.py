from math import pi
from typing import List, Tuple


def get_square(events: List[Tuple[int, int]], rectangles_count: int, rmin: int, rmax: int) -> int:
    """
    Функция которая вычисляет площадь пересечения всех полярных прямоугольников.

    :param events: список событий (величина угла, порядковый номер события
    (отрицательный, если это начало прямоугольника))
    :type events: List[Tuple[int, int]]
    :param rectangles_count: количество прямоугольников
    :type rectangles_count: int
    :param rmin: минимальный радиус пересечения прямоугольников
    :type rmin: int
    :param rmax: максимальный радиус пересечения прямоугольников
    :type rmax: int

    :return: площадь пересечения всех прямоугольников
    :rtype: int
    """
    used_segments = set()
    segments_count = 0
    for event in events:
        if event[1] < 0:
            segments_count += 1
            used_segments.add(-event[1])
        elif event[1] in used_segments:
            segments_count -= 1

    ans = 0
    for i in range(len(events)):
        event = events[i]
        if event[1] < 0:
            segments_count += 1
        else:
            segments_count -= 1
        if segments_count == rectangles_count:
            if i < len(events) - 1:
                ans += (events[i + 1][0] - events[i][0]) * (rmax ** 2 - rmin ** 2) / 2
            else:
                ans += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * (rmax ** 2 - rmin ** 2) / 2

    return ans


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())
    events = []
    rmin = 0
    rmax = float('inf')
    for i in range(1, N + 1):
        r1, r2, phi1, phi2 = map(float, input().split())
        rmin = max(rmin, r1)
        rmax = min(rmax, r2)
        events.append((phi1, -i))
        events.append((phi2, i))
    events.sort()

    print(get_square(events, N, rmin, rmax))


if __name__ == '__main__':
    main()
