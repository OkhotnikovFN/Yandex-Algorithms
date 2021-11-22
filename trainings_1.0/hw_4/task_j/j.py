import re


def get_synonym(file_name: str) -> str:
    """
    Функция которая которая по приведенной программе определяет наиболее часто используемый в ней идентификатор.

    :param file_name: имя файла с данными
    :type file_name: str

    :return: наиболее часто используемый идентификатор
    :rtype: str
    """
    file = open(file_name, 'r')

    n, case_sens, first_digit = file.readline().strip().split()
    n = int(n)
    case_sens = case_sens == 'yes'
    first_digit = first_digit == 'yes'
    if first_digit:
        key_word_pattern = r'\b[a-zA-Z0-9_]+\b'
    else:
        key_word_pattern = r'\b[a-zA-Z_]+[a-zA-Z0-9_]*\b'

    key_words = set()
    for _ in range(n):
        key_word = file.readline().strip()
        if not case_sens:
            key_word = key_word.lower()
        key_words.add(key_word)

    words_counts = {}
    word_pos_id = 1
    for line in file.readlines():
        words = re.findall(key_word_pattern, line)
        for word in words:
            if not case_sens:
                word = word.lower()
            if word in key_words:
                continue
            if not word.isdigit():
                if word in words_counts:
                    words_counts[word][0] += 1
                else:
                    words_counts[word] = [1, word_pos_id]
                    word_pos_id += 1
    file.close()

    result = ''
    max_count = 0
    pos = 0
    for word, val in words_counts.items():
        if val[0] > max_count:
            max_count = val[0]
            result = word
            pos = val[1]
        if val[0] == max_count and val[1] < pos:
            result = word
            pos = val[1]

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    file_name = 'input.txt'
    print(get_synonym(file_name))


if __name__ == '__main__':
    main()
