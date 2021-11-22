from typing import List

DISTANCE_END = 5


def determine_place(n: int, distance_list: List[int]) -> int:
    """
    Функция которая определяет, максимально высокое место участника.

    :param n: длинна входного списка с расстояниями бросков участников
    :type n: int
    :param distance_list: список с расстояниями бросков участников
    :type distance_list: List[int]

    :return: максимально высокое место участника, или 0,
    если не существует ни одного участника, который удовлетворяет условиям
    :rtype: int
    """
    required_distance = 0
    max_distance = max(distance_list)
    winner_flag = False

    for player_number in range(1, n - 1):
        player_distance = distance_list[player_number]
        if distance_list[player_number - 1] == max_distance:
            winner_flag = True
        if player_distance % 10 == DISTANCE_END and winner_flag and player_distance > distance_list[player_number + 1]:
            required_distance = max(player_distance, required_distance)

    if not required_distance:
        return 0

    required_player_place = 1
    for player_distance in distance_list:
        if player_distance > required_distance:
            required_player_place += 1
    return required_player_place


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    distance_list = list(map(int, input().split()))
    print(determine_place(n, distance_list))


if __name__ == '__main__':
    main()
