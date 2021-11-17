def get_synonym(word: str, words_dict: dict) -> str:
    """
    Функция которая получает синоним данного слова.
        Параметры:
            :param word: список который необходимо проверить
            :type word: str
            :param words_dict: словарь синонимов
            :type words_dict: dict
        Возвращаемое значение:
            :return: синоним к данному слову
            :rtype: str
    """
    return words_dict[word]


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    words_dict = {}
    for _ in range(n):
        word_1, word_2 = input().split()
        words_dict[word_1] = word_2
        words_dict[word_2] = word_1
    word = input()

    print(get_synonym(word, words_dict))


if __name__ == '__main__':
    main()
