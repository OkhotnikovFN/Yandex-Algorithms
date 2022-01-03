from typing import List, Tuple


def get_votes_number(file_name) -> List[Tuple[str, int]]:
    """
    Функция которая считает количество голосов каждого кандидата.

    :param file_name: имя файла с данными
    :type file_name: str

    :return: отсортированный список (имя кандидата, количество голосов)
    :rtype: List[Tuple[str, int]]
    """
    candidates = {}

    with open(file_name) as file:
        for line in file:
            name, voices = line.split()
            if name in candidates:
                candidates[name] += int(voices)
            else:
                candidates[name] = int(voices)

    result = []
    for key in sorted(list(candidates)):
        result.append((key, candidates[key]))

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    result = get_votes_number('input.txt')
    for value in result:
        print(*value)


if __name__ == '__main__':
    main()
