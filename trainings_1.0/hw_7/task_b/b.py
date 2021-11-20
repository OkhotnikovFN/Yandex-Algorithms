from typing import List, Tuple, Union

SEGMENT_START = -1
SEGMENT_END = 1
POINT = 0


def get_count_uniq_numbers(events: List[Tuple[int, int, Union[int]]], points_count: int) -> List[int]:
    """
    Функция которая вычисляет для каждой точки ко скольким отрезкам она принадлежит.
        Параметры:
            :param events: список c событий, в котором указана точка на отрезке, и тип события связанный с этой точкой,
            для исследуемых точек, еще указан порядковый номер точки
            :type events: List[Tuple[int, int, Union[int]]]
            :param points_count: количество исследуемых точек
            :type points_count: int
        Возвращаемое значение:
            :return: список с количеством отрезком, к которым принадлежат точки
            :rtype: List[int]
    """
    result = [0] * points_count
    cur_covered_segments_count = 0

    for event in events:
        if event[1] == SEGMENT_START:
            cur_covered_segments_count += 1
        elif event[1] == SEGMENT_END:
            cur_covered_segments_count -= 1
        elif event[1] == POINT:
            index = event[2]
            result[index] = cur_covered_segments_count

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, m = map(int, input().split())

    coords = []
    for _ in range(n):
        start, end = sorted(list(map(int, input().split())))
        coords.append((start, SEGMENT_START))
        coords.append((end, SEGMENT_END))

    points = map(int, input().split())

    for i, point in enumerate(points):
        coords.append((point, POINT, i))

    coords.sort()

    print(*get_count_uniq_numbers(coords, m))


if __name__ == '__main__':
    main()
