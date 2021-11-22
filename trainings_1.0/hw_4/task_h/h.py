def make_dict(s: str) -> dict:
    """
    Функция которая из строки создает словарь с количеством вхождений каждого символа в строке.

    :param s: исследуемая строка
    :type s: s

    :return: словарь с количеством вхождений каждого символа в строке
    :rtype: dict
    """
    s_dict = {}
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
    return s_dict


def match_dict(dict_1: dict, dict_2: dict) -> int:
    """
    Функция которая сравнивает два словаря.

    :param dict_1: первый словарь
    :type dict_1: dict
    :param dict_2: второй словарь
    :type dict_2: dict

    :return: количество совпадений значений из dict_1 в dict_2
    :rtype: int
    """
    matches = 0
    for c in dict_1:
        if c in dict_2 and dict_1[c] == dict_2[c]:
            matches += 1
    return matches


def modify_dict(dict_string: dict, dict_word: dict, symbol: str, count_modifier: int) -> int:
    """
    Функция которая модифицирует словарь текущего слова в тексте
    и изменяет количество совпадений dict_word и dict_string.

    :param dict_string: словарь текущего слова в тексте
    :type dict_string: dict
    :param dict_word: словарь искомого слова
    :type dict_word: dict
    :param symbol: изменяемый символ
    :type symbol: dict
    :param count_modifier: модификатор, изменяющий количество вхождений символа symbol в словарь dict_string
    :type count_modifier: int

    :return: изменение количества совпадений dict_word и dict_string
    :rtype: int
    """
    ans = 0
    if symbol not in dict_string:
        dict_string[symbol] = 0
    if symbol in dict_word and dict_string[symbol] == dict_word[symbol]:
        ans = -1
    dict_string[symbol] += count_modifier
    if symbol in dict_word and dict_string[symbol] == dict_word[symbol]:
        ans = 1
    return ans


def get_number_of_occurrences(len_word: int, len_string: int, word: str, researched_string: str) -> int:
    """
    Функция которая подсчитывает количество всех возможных вхождений слова word в строку researched_string.

    :param len_word: длинна слова
    :type len_word: int
    :param len_string: длинна исследуемой строки
    :type len_string: dict
    :param word: символы слова
    :type word: str
    :param researched_string: исследуемая строка
    :type researched_string: str

    :return: количество всевозможных вхождений word в researched_string
    :rtype: int
    """
    dict_word = make_dict(word)
    dict_string = make_dict(researched_string[:len_word])
    matching_letters = match_dict(dict_word, dict_string)
    counter = 0

    if matching_letters == len(dict_word):
        counter += 1

    for shift in range(len_word, len_string):
        matching_letters += modify_dict(dict_string, dict_word, researched_string[shift - len_word], -1)
        matching_letters += modify_dict(dict_string, dict_word, researched_string[shift], 1)
        if matching_letters == len(dict_word):
            counter += 1

    return counter


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    len_word, len_string = map(int, input().split())
    word = input()
    researched_string = input()
    print(get_number_of_occurrences(len_word, len_string, word, researched_string))


if __name__ == '__main__':
    main()
