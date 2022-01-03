from typing import List


def get_words(file_name: str) -> List[str]:
    """
    Функция которая определяет частоту появления слов в тексте.

    :param file_name: имя файла с текстом
    :type file_name: str

    :return: список слов, отсортированный по убыванию их появления в тексте
    :rtype: List[str]
    """
    words_dict = {}
    with open(file_name) as file:
        for line in file:
            names = line.split()
            for name in names:
                if name in words_dict:
                    words_dict[name] += 1
                else:
                    words_dict[name] = 1

    words_count_dict = {}
    for key, val in words_dict.items():
        if val in words_count_dict:
            words_count_dict[val].append(key)
        else:
            words_count_dict[val] = [key]

    for key in words_count_dict:
        words_count_dict[key] = sorted(words_count_dict[key])
    words_list = sorted(words_count_dict.items(), key=lambda x: x[0], reverse=True)

    result = []
    for small_list in words_list:
        for word in small_list[1]:
            result.append(word)

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    print(*get_words('input.txt'), sep='\n')


if __name__ == '__main__':
    main()
