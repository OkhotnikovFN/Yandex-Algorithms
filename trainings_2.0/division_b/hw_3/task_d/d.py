from typing import List


def find_possible_nums(max_num) -> List[int]:
    """
    Функция которая определяет числа, которые мог загадать Август.

    :param max_num: максимальное число, которое мог загадать Август
    :type max_num: int

    :return: список возможных чисел
    :rtype: List[int]
    """

    possible_nums = set(range(1, max_num + 1))

    while True:
        cur_num_set = input()
        if cur_num_set != 'HELP':
            cur_num_set = set(map(int, cur_num_set.split()))
            answer = input()
            if answer == 'YES':
                possible_nums.intersection_update(cur_num_set)
            else:
                possible_nums.difference_update(cur_num_set)
        else:
            break

    return sorted([x for x in possible_nums])


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    max_num = int(input())
    print(*find_possible_nums(max_num))


if __name__ == '__main__':
    main()
