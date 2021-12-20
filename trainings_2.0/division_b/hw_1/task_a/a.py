def get_verdict(iteractor, checker, exit_code) -> int:
    """
    Функция которая определяет итоговый вердикт.

    :param iteractor: вердикт итерактора
    :type iteractor: int
    :param checker: вердикт чекера
    :type checker: int
    :param exit_code: код завершения задачи
    :type exit_code: int

    :return: вердикт основанный на входных данных
    :rtype: int
    """

    if iteractor == 0:
        if exit_code != 0:
            return 3
        else:
            return checker

    if iteractor == 1:
        return checker

    if iteractor == 4:
        if exit_code != 0:
            return 3
        else:
            return 4

    if iteractor == 6:
        return 0

    if iteractor == 7:
        return 1

    return iteractor


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    r = int(input())
    i = int(input())
    c = int(input())
    print(get_verdict(i, c, r))


if __name__ == '__main__':
    main()
