def get_chars_count(input_string: str) -> int:
    """
    Функция которая определяет количество букв, которые необходимо заменить в исходной строке, чтобы получить палиндром.

    :param input_string: проверяемая строка
    :type input_string: str

    :return: количество букв
    :rtype: int
    """
    counter = 0

    for index in range(len(input_string) // 2):
        if input_string[index] != input_string[-index - 1]:
            counter += 1

    return counter


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    input_string = input()
    print(get_chars_count(input_string))


if __name__ == '__main__':
    main()
