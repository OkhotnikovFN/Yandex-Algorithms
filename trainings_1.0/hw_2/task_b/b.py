END_SEQUENCE = -2 * 10 ** 9


def check_sequence() -> str:
    """
    Функция которая проверяет последовательность и определяет ее тип.

    :return: строковое значение, определяющее тип последовательности
    :rtype: str
    """

    sequence_item = int(input())
    if sequence_item == END_SEQUENCE:
        return 'RANDOM'

    const_flag = True
    ascend_flag = True
    weak_ascend_flag = True
    descend_flag = True
    weak_descend_flag = True

    while sequence_item != END_SEQUENCE:
        prev_array_item = sequence_item
        sequence_item = int(input())

        if sequence_item == END_SEQUENCE:
            break

        if sequence_item != prev_array_item:
            const_flag = False
        if sequence_item <= prev_array_item:
            ascend_flag = False
        if sequence_item < prev_array_item:
            weak_ascend_flag = False
        if sequence_item >= prev_array_item:
            descend_flag = False
        if sequence_item > prev_array_item:
            weak_descend_flag = False

        if not const_flag and not ascend_flag and not weak_ascend_flag and not descend_flag and not sequence_item:
            break

    if const_flag:
        return 'CONSTANT'
    elif ascend_flag:
        return 'ASCENDING'
    elif weak_ascend_flag:
        return 'WEAKLY ASCENDING'
    elif descend_flag:
        return 'DESCENDING'
    elif weak_descend_flag:
        return 'WEAKLY DESCENDING'
    else:
        return 'RANDOM'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    print(check_sequence())


if __name__ == '__main__':
    main()
