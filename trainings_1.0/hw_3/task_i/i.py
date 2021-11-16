from typing import Tuple, Set


def define_languages(n: int) -> Tuple[int, Set[str], int, Set[str]]:
    """
    Функция которая определяет какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
        Параметры:
            :param n: количество школьников
            :type n: int
        Возвращаемое значение:
            :return: количество языков, которые знают все школьники, список таких языков,
            количество языков, которые знает хотя бы один школьник, список таких языков.
            :rtype: Tuple[int, Set[str], int, Set[str]]
    """
    all_languages = set()
    list_all_students = []

    for n in range(n):
        m = int(input())
        individual_languages_set = set()
        for m in range(m):
            language = input()
            all_languages.add(language)
            individual_languages_set.add(language)
        list_all_students.append(individual_languages_set)

    all_know_languages = list_all_students[0].intersection(*list_all_students)

    return len(all_know_languages), all_know_languages, len(all_languages), all_languages


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    result = define_languages(n)
    print(result[0])
    print(*result[1], sep='\n')
    print(result[2])
    print(*result[3], sep='\n')


if __name__ == '__main__':
    main()
