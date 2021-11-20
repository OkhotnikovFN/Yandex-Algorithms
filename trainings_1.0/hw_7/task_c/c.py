from typing import List, Tuple


STUDENT_START = -1
STUDENT_END = 1


def get_students_count(events: List[Tuple[int, int, int]], students_count: int) -> Tuple[int, List[int]]:
    """
    Функция которая вычисляет необходимое количество билетов и вариант раздачи билетов.
        Параметры:
            :param events: список событий в котором указаны координата студента, тип события, порядковый номер студента
            :type events: List[Tuple[int, int, int]]
            :param students_count: количество студентов
            :type students_count: int
        Возвращаемое значение:
            :return: количество билетов, список с вариантом раздачи билетов
            :rtype: Tuple[int, List[int]]
    """
    max_exam_number = 0
    reused_tickets = []
    exam_tickets = [0] * students_count

    for x, event, original_order in events:
        if event == STUDENT_START:
            if len(reused_tickets) == 0:
                max_exam_number += 1
                next_exam_number = max_exam_number
            else:
                next_exam_number = reused_tickets.pop(0)
            exam_tickets[original_order] = next_exam_number
        elif event == STUDENT_END:
            student_exam_number = exam_tickets[original_order]
            reused_tickets.append(student_exam_number)

    return max_exam_number, exam_tickets


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, d = map(int, input().split())
    students = list(map(int, input().split()))

    events = []
    for i, x in enumerate(students):
        events.append((x, STUDENT_START, i))
        events.append((x + d, STUDENT_END, i))

    sorted_events = sorted(events)

    result = get_students_count(sorted_events, n)

    print(result[0])
    print(*result[1])


if __name__ == '__main__':
    main()
