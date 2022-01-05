from typing import Tuple, List


def get_segments(input_segments: List[Tuple[int, int]], segments_end: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Функция которая вычисляет минимально количество отрезков, необходимое для полного покрытия исходного отрезка.

    :param input_segments: список отрезков (начало, конец) из которых нужно выбрать нужные
    :type input_segments: List[Tuple[int, int]]
    :param segments_end: конец исходного отрезка
    :type segments_end: int

    :return: количество отрезков с координатами начала и конца каждого отрезка, или None, если решения нет
    :rtype: Tuple[int, List[Tuple[int, int]]]
    """
    min_segment_list = []
    now_right = 0
    next_right = 0
    now_best = 0, 0
    for segment in input_segments:
        if segment[0] > now_right:
            min_segment_list.append(now_best)
            now_right = next_right
            if now_right >= segments_end:
                break
        if segment[0] <= now_right and segment[1] > next_right:
            next_right = segment[1]
            now_best = segment

    if now_right < segments_end:
        now_right = next_right
        min_segment_list.append(now_best)

    if now_right >= segments_end:
        return len(min_segment_list), min_segment_list


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    M = int(input())

    input_segments = []
    while True:
        L, R = map(int, input().split())
        if L == R == 0:
            break
        input_segments.append((L, R))
    input_segments.sort()

    result = get_segments(input_segments, M)
    if result:
        print(result[0])
        for segment in result[1]:
            print(*segment)
    else:
        print('No solution')


if __name__ == '__main__':
    main()
