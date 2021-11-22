import sys


def get_count_uniq_words(text: str) -> int:
    """
    Функция которая определяет количество уникальных слов в тексте.

    :param text: входной текст
    :type text: str

    :return: количество уникальных слов в тексте
    :rtype: int
    """
    words_list = text.split()
    words_set = set(words_list)

    return len(words_set)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    text = sys.stdin.read()
    print(get_count_uniq_words(text))


if __name__ == '__main__':
    main()
