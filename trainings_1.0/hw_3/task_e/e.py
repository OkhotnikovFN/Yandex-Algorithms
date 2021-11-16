from typing import Set


def get_count_required_buttons(buttons: Set[str], number: str) -> int:
    """
    Функция которая определяет количество кнопок, которые необходимо добавить.
        Параметры:
            :param buttons: существующие кнопки
            :type buttons: List[str]
            :param number: число, которое нужно напечатать
            :type number: str
        Возвращаемое значение:
            :return: количество кнопок, которые необходимо добавить
            :rtype: int
    """
    number_set = set(number)
    return len(number_set - buttons)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    buttons = set(input().split())
    number = input()
    print(get_count_required_buttons(buttons, number))


if __name__ == '__main__':
    main()
