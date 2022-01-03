from typing import List, Tuple


def get_votes_count(file_name) -> List[Tuple[str, int]]:
    """
    Функция которая вычисляет количество голосов в парламенте, полученных партиями.

    :param file_name: имя файла с партиями
    :type file_name: str

    :return: список партий с количество отданным партиям голосов
    :rtype: List[Tuple[str, int]]
    """
    list_of_parties = []
    all_voices = 0

    with open(file_name) as file:
        for line in file:
            data = line.split()
            voices = int(data[-1])
            all_voices += voices
            name = ' '.join(data[:-1])
            list_of_parties.append((name, voices))

    dict_of_parties = {}
    all_places = 0

    for party in list_of_parties:
        places_count = party[1] * 450 // all_voices
        all_places += places_count
        dict_of_parties[party[0]] = places_count

    remaining_seats = 450 - all_places
    if remaining_seats:
        new_list_of_parties = sorted(list_of_parties, key=lambda x: x[1] * 450 % all_voices, reverse=True)
        for i in range(remaining_seats):
            dict_of_parties[new_list_of_parties[i][0]] += 1

    result = []
    for party in list_of_parties:
        result.append((party[0], dict_of_parties[party[0]]))

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    result = get_votes_count('input.txt')
    for val in result:
        print(*val)


if __name__ == '__main__':
    main()
