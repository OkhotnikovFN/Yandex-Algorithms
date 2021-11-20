from typing import List, Tuple

BOX_OFFICE_CLOSE = -1
BOX_OFFICE_OPEN = 1


def get_offices_count(events: List[Tuple[int, int, int]], offices_count: int) -> int:
    """
    Функция которая вычисляет суммарное время, которое работаю все кассы.
        Параметры:
            :param events: список событий в которых указан момент времени, тип события, номер кассы
            :type events: List[Tuple[int, int, int]]
            :param offices_count: количество не круглосуточно работающих офисов
            :type offices_count: int
        Возвращаемое значение:
            :return: суммарное время, когда работаю все кассы
            :rtype: int
    """
    if offices_count == 0:
        return 24 * 60

    opened_box_offices = set()
    for event in events:
        if event[1] == BOX_OFFICE_CLOSE:
            if event[2] in opened_box_offices:
                opened_box_offices.remove(event[2])
        elif event[1] == BOX_OFFICE_OPEN:
            opened_box_offices.add(event[2])

    count_opened_box_offices = len(opened_box_offices)
    start_time = 0
    result = 0
    for event in events:
        if event[1] == BOX_OFFICE_OPEN:
            count_opened_box_offices += 1
            if count_opened_box_offices == offices_count:
                start_time = event[0]
        elif event[1] == BOX_OFFICE_CLOSE:
            if count_opened_box_offices == offices_count:
                result += event[0] - start_time
            count_opened_box_offices -= 1
    if count_opened_box_offices == offices_count:
        result += 60 * 24 - start_time

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    events = []
    offices_count = 0
    for i in range(n):
        hours_1, minutes_1, hours_2, minutes_2 = map(int, input().split())
        time_1 = hours_1 * 60 + minutes_1
        time_2 = hours_2 * 60 + minutes_2
        if time_1 != time_2:
            offices_count += 1
            events.append((time_1, BOX_OFFICE_OPEN, i))
            events.append((time_2, BOX_OFFICE_CLOSE, i))
    events.sort()

    print(get_offices_count(events, offices_count))


if __name__ == '__main__':
    main()
