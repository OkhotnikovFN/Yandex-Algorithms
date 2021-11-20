from typing import List, Tuple


START_SCAN = -1
END_SCAN = 1


def get_students_count(events: List[Tuple[int, int]], students_count: int) -> int:
    """
    Функция которая вычисляет количество студентов, которые будут списывать.
        Параметры:
            :param events: список c событий, в котором указан номер парты
            и тип события, связанный с этой партой
            :type events: List[Tuple[int, int]
            :param students_count: общее количество студентов
            :type students_count: int
        Возвращаемое значение:
            :return: количество студентов, которые будут списывать
            :rtype: int
    """
    monitored_desks_first = 0
    current_auditor_count = 0
    monitored_desks = 0

    for event in events:
        if event[1] == START_SCAN:
            current_auditor_count += 1
            if current_auditor_count == 1:
                monitored_desks_first = event[0]
        elif event[1] == END_SCAN:
            current_auditor_count -= 1
            if current_auditor_count == 0:
                monitored_desks += event[0] - monitored_desks_first + 1

    return students_count - monitored_desks


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, m = map(int, input().split())

    events = []
    for _ in range(m):
        start, end = map(int, input().split())
        events.append((start, START_SCAN))
        events.append((end, END_SCAN))
    events.sort()

    print(get_students_count(events, n))


if __name__ == '__main__':
    main()
