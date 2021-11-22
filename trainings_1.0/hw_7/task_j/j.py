from typing import List, Tuple, Union, Set

START_HEIGHT = 1
END_HEIGHT = - 1


def get_min_blocks_count(events: List[Tuple[List[int], int, int, int]], blocks_count: int,
                         complex_width: int, complex_length: int) -> Union[str, Tuple[str, int, Set[int]]]:
    """
    Функция которая вычисляет минимально необходимое количество блоков.

    :param events: список событий, в котором указаны, высота, тип события (начало, конец блока),
    площадь блока по осям x и y, индекс блока
    :type events: List[Tuple[List[int], int, int, int]]
    :param blocks_count: исходное количество блоков
    :type blocks_count: int
    :param complex_width: ширина комплекса
    :type complex_width: int
    :param complex_length: длина комплекса
    :type complex_length: int

    :return: ответ, возможно ли это сделать и если да, то количество блоков и множество этих блоков
    :rtype: Union[str, Tuple[str, int, Set[int]]]
    """
    total_area = complex_width * complex_length
    min_used = blocks_count + 1
    now_used = 0
    now_area = 0

    for event in events:
        if event[1] == START_HEIGHT:
            now_used += 1
            now_area += event[2]
            if now_area == total_area and now_used < min_used:
                min_used = now_used
        elif event[1] == END_HEIGHT:
            now_used -= 1
            now_area -= event[2]

    if min_used == blocks_count + 1:
        return 'NO'

    used_blocks = set()
    for event in events:
        if event[1] == START_HEIGHT:
            now_used += 1
            used_blocks.add(event[3])
            now_area += event[2]
            if now_area == total_area and now_used == min_used:
                break
        elif event[1] == END_HEIGHT:
            now_used -= 1
            used_blocks.remove(event[3])
            now_area -= event[2]

    return 'YES', min_used, used_blocks


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, w, l = map(int, input().split())

    events = []
    for i in range(1, n + 1):
        x1, y1, z1, x2, y2, z2 = map(int, input().split())
        area = abs(x2 - x1) * abs(y2 - y1)
        events.append((z1, START_HEIGHT, area, i))
        events.append((z2, END_HEIGHT, area, i))
    events.sort()

    result = get_min_blocks_count(events, n, w, l)
    if isinstance(result, str):
        print(result)
    else:
        print(result[0])
        print(result[1])
        for block in result[2]:
            print(block)


if __name__ == '__main__':
    main()
