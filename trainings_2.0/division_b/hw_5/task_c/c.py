from typing import List, Tuple


def get_groups_count(n: int, groups: List[str], audiences: List[str]) -> Tuple[int, List[int]]:
    """
    Функция которая определяет количество групп, которые удалось разместить и распределение групп по аудиториям.

    :param n: количество групп
    :type n: int
    :param groups: список групп с количеством учащихся
    :type groups: List[str]
    :param audiences: список аудиторий с количеством компьютеров
    :type audiences: List[str]

    :return: количество групп, которые удалось разместить, и распределение групп по аудиториям
    :rtype: Tuple[int, List[str]]
    """

    groups_list = []
    for index, val in enumerate(groups):
        groups_list.append((int(val), index))
    groups_list.sort(reverse=True)

    audiences_list = []
    for index, val in enumerate(audiences):
        audiences_list.append((int(val), index))
    audiences_list.sort(reverse=True)

    count = 0
    group_in_audience_dict = {}
    aud_index = 0

    for group_index in range(n):
        group = groups_list[group_index][0]
        audience = audiences_list[aud_index][0]
        if audience >= group + 1:
            count += 1
            group_in_audience_dict[groups_list[group_index][1]] = audiences_list[aud_index][1] + 1
            aud_index += 1

    result = []
    for index in range(n):
        result.append(group_in_audience_dict.get(index, 0))

    return count, result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, m = map(int, input().split())
    groups = input().split()
    audiences = input().split()

    result = get_groups_count(n, groups, audiences)
    print(result[0])
    print(*result[1])


if __name__ == '__main__':
    main()
