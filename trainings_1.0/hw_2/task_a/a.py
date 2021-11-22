from typing import List


def check_list(checked_list: List) -> str:
    """
    Функция проверяющая список на монотонность возрастания.

    :param checked_list: список который необходимо проверить
    :type checked_list: str

    :return: строковое значение, является ли список монотонно возрастающим
    :rtype: str
    """
    for i in range(1, len(checked_list)):
        if checked_list[i] <= checked_list[i - 1]:
            return 'NO'
    return 'YES'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    checked_list = input().split()
    print(check_list(checked_list))


if __name__ == '__main__':
    main()
