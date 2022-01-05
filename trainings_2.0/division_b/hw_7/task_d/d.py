from typing import List, Tuple

START = -1
END = 1
CAT = 0
CATS_COUNT = 0


def get_cats_count_be_segment(events: List[Tuple[int, int, int]], segments: List[List[int]]) -> List[int]:
    """
    Функция которая вычисляет количество котят на каждом отрезке.

    :param events: события, начала отрезка, конца отрезка, появление кота
    :type events: List[Tuple[int, int, int]]
    :param segments: список отрезков с координатами и количеством котов а отрезке
    :type segments: List[List[int]]

    :return: количество котов для каждого отрезка
    :rtype: List[int]
    """
    cats_count = 0
    for point, code, index in events:
        if code == START:
            segments[index][2] = cats_count

        if code == END:
            segments[index][2] = cats_count - segments[index][2]

        if code == CAT:
            cats_count += 1

    del events

    return [segment[2] for segment in segments]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, m = map(int, input().split())
    cats = list(map(int, input().split()))

    events = []
    segments = []

    for i in range(m):
        l, r = map(int, input().split())
        events.append((l, START, i))
        events.append((r, END, i))
        segments.append([l, r, CATS_COUNT])

    for cat in cats:
        events.append((cat, CAT, 0))

    events.sort()

    print(*get_cats_count_be_segment(events, segments))


if __name__ == '__main__':
    main()
