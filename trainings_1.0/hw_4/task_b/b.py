from typing import List


def get_count_number_of_repetitions(file_name: str) -> List[int]:
    """
    Функция которая считывает текст и проверяет сколько раз слово встречалось в тексте ранее.

    :param file_name: название файла
    :type file_name: str

    :return: список с ответами
    :rtype: List[int]
    """
    answer = []
    words_dict = {}
    with open(file_name) as text:
        for line in text:
            for word in line.split():
                if word in words_dict:
                    answer.append(words_dict[word])
                    words_dict[word] += 1
                else:
                    answer.append(0)
                    words_dict[word] = 1
    return answer


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    file_name = 'input.txt'
    print(*get_count_number_of_repetitions(file_name))


if __name__ == '__main__':
    main()
