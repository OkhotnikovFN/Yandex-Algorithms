from typing import List, Tuple


def find_sequence(n: int, checked_list: List[int]) -> Tuple[int, str]:
    """
    Функция которая определяет, какое минимальное количество и каких чисел надо приписать
    в конец последовательности, чтобы она стала симметричной.
        Параметры:
            :param n: длинна входной последовательности
            :type n: int
            :param checked_list: исследуемая последовательность чисел
            :type checked_list: List[int]
        Возвращаемое значение:
            :return: длинна требуемой последовательности и строковое представление самой последовательности
            :rtype: Tuple[int, str]
    """
    symmetrical_sequence_length = 0
    right_index = -1

    for left_index in range(n):
        if checked_list[left_index] == checked_list[right_index]:
            right_index -= 1
            symmetrical_sequence_length += 1
        else:
            right_index = -1
            symmetrical_sequence_length = 0

    required_length = n - symmetrical_sequence_length
    if required_length:
        return required_length, ' '.join(map(str, checked_list[required_length - 1::-1]))
    else:
        return required_length, ''


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    checked_list = list(map(int, input().split()))
    result = find_sequence(n, checked_list)
    if result[0]:
        print(result[0])
        print(result[1])
    else:
        print(result[0])


if __name__ == '__main__':
    main()
