def check_sequence(seq: str) -> str:
    """
    Функция которая проверяет скобочную последовательность на корректность.

    :param seq: последовательность
    :type seq: str

    :return: ответ 'YES' - если правильная, 'NO' - если нет
    :rtype: str
    """
    open_parenthesis = 0
    close_parenthesis = 0
    for parenthesis in seq:
        if parenthesis == '(':
            open_parenthesis += 1
        else:
            close_parenthesis += 1
        if open_parenthesis - close_parenthesis < 0:
            return 'NO'
    if open_parenthesis > close_parenthesis:
        return 'NO'
    return 'YES'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    parenthesis_sequence = input()
    print(check_sequence(parenthesis_sequence))


if __name__ == '__main__':
    main()
