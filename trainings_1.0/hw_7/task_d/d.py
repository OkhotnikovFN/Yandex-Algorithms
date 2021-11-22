from typing import List, Tuple


CLIP_LENGTH = 5
INCOME = -1
OUTCOME = 1


def find_time_moments(events: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
    """
    Функция которая вычисляет количество покупателей, увидевших рекламу, и моменты времени, когда надо включить рекламу.

    :param events: список событий, в которых указан момент времени, тип этого события, номер покупателя
    :type events: List[Tuple[int, int, int]]

    :return: количество покупателей, увидевших рекламу, и моменты времени, когда надо включить рекламу.
    :rtype: Tuple[int, int, int]
    """
    if len(events) == 0:
        return 0, 10, 20
    elif len(events) == 2:
        return 1, events[0][0], events[0][0] + 10
    else:
        customers_count = 0
        first_start, second_start = 0, 0
        first_customers = set()
        for i in range(len(events)):
            event_1 = events[i]
            if event_1[1] == INCOME:
                first_customers.add(event_1[2])
                if len(first_customers) > customers_count:
                    customers_count = len(first_customers)
                    first_start = event_1[0]
                    second_start = event_1[0] + CLIP_LENGTH
            second_count = 0
            for j in range(i + 1, len(events)):
                event_2 = events[j]
                if event_2[1] == INCOME:
                    second_count += 1
                if event_2[0] - CLIP_LENGTH >= event_1[0] and len(first_customers) + second_count > customers_count:
                    customers_count = len(first_customers) + second_count
                    first_start, second_start = event_1[0], event_2[0]
                if event_2[1] == OUTCOME and event_2[2] not in first_customers:
                    second_count -= 1
            if event_1[1] == OUTCOME:
                first_customers.remove(event_1[2])
        return customers_count, first_start, second_start


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    events = []
    for i in range(n):
        income, outcome = map(int, input().split())
        if outcome - income >= CLIP_LENGTH:
            events.append((income, INCOME, i))
            events.append((outcome - CLIP_LENGTH, OUTCOME, i))
    events.sort()

    print(*find_time_moments(events))


if __name__ == '__main__':
    main()
