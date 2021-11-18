from collections import defaultdict
from typing import Tuple


def find_substring(input_str: str, k: int) -> Tuple[int, int]:
    """
    Функция которая находит максимальную по длине подстроку данной строки.
        Параметры:
            :param input_str: исходная строка
            :type input_str: str
            :param k: максимальное количество вхождений символа в искомую подстроку
            :type k: int
        Возвращаемое значение:
            :return: длинна искомой подстроки и номер её первого символа
            :rtype: Tuple[int, int]
    """
    best_result = (float('-inf'), 0)
    left = 0
    counter = defaultdict(int)
    substring_length = 0
    for right_char in input_str:
        while counter[right_char] >= k:
            counter[input_str[left]] -= 1
            substring_length -= 1
            left += 1

        counter[right_char] += 1
        substring_length += 1
        if substring_length > best_result[0]:
            best_result = (substring_length, left + 1)

    return best_result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, k = map(int, input().split())
    string = input()
    print(*find_substring(string, k))


if __name__ == '__main__':
    main()
