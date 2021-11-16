from typing import List


def get_count_uniq_numbers(input_list: List[int]) -> int:
    """
    Функция которая проверяет количество уникальных чисел в списке.
        Параметры:
            :param input_list: список который необходимо проверить
            :type input_list: List[int]
        Возвращаемое значение:
            :return: количество уникальных чисел в списке
            :rtype: int
    """
    return len(set(input_list))


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    checked_list = list(map(int, input().split()))
    print(get_count_uniq_numbers(checked_list))


if __name__ == '__main__':
    main()
