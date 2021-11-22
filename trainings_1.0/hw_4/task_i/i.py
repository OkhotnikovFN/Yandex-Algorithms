def get_errors_count(words_dict: dict, text: str) -> int:
    """
    Функция которая определяет количество ошибок в тексте.

    :param words_dict: словарь слов с правильно расставленными ударениями
    :type words_dict: dict
    :param text: проверяемый текст
    :type text: str

    :return: количество найденных ошибок
    :rtype: int
    """
    errors_count = 0
    for word in text.split():
        word_lower = word.lower()
        if word_lower in words_dict:
            if word not in words_dict[word_lower]:
                errors_count += 1
        else:
            accents = 0
            for char in word:
                if char.isupper():
                    accents += 1
            if accents != 1:
                errors_count += 1

    return errors_count


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    words_dict = {}
    for _ in range(n):
        word = input()
        word_lower = word.lower()
        if word_lower in words_dict:
            words_dict[word_lower].add(word)
        else:
            words_dict[word_lower] = {word}
    text = input()

    print(get_errors_count(words_dict, text))


if __name__ == '__main__':
    main()
