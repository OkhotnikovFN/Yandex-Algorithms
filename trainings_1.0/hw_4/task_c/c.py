def get_word(file_name) -> str:
    """
    Функция которая находит наиболее встречающееся слово в тексте.
        Параметры:
            :param file_name: имя файла с текстом
            :type file_name: str
        Возвращаемое значение:
            :return: наиболее встречающееся слово
            :rtype: str
    """
    max_entries = 0
    words_dict = {}
    with open(file_name) as text:
        for line in text:
            for word in line.split():
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
                max_entries = max(max_entries, words_dict[word])

    possible_words = []
    for key, val in words_dict.items():
        if val == max_entries:
            possible_words.append(key)
    answer = possible_words[0]
    for word in possible_words:
        if word < answer:
            answer = word

    return answer


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    file_name = 'input.txt'
    print(get_word(file_name))


if __name__ == '__main__':
    main()
