from typing import Tuple, List


def get_time_for_blow(balloons_count: int, people_count: int) -> Tuple[int, List[int]]:
    """
    Функция которая вычисляет необходимое время для надувания всех шариков
    и выводи список, кто сколько шариков надул.

    :param balloons_count: необходимое количество шариков
    :type balloons_count: int
    :param people_count: количество людей, надувающих шарики
    :type people_count: int

    :return: необходимое время и список с количеством надутых шариков
    :rtype: Tuple[int, List[int]
    """
    people = [0] * people_count

    if not balloons_count:
        return 0, people

    events = []
    for i in range(people_count):
        time_for_blow, balloons_without_rest, rest_time = map(int, input().split())
        time_stamp = time_for_blow
        for balloon in range(1, balloons_count + 1):
            events.append((time_stamp, i))
            if balloon % balloons_without_rest == 0:
                time_stamp += rest_time
            time_stamp += time_for_blow
    events.sort()

    for event in events[:balloons_count]:
        people[event[1]] += 1
    return events[balloons_count - 1][0], people


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    m, n = map(int, input().split())
    result = get_time_for_blow(m, n)
    print(result[0])
    print(*result[1])


if __name__ == '__main__':
    main()
