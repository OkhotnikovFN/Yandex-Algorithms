import datetime
from typing import Tuple, List, Set

BIRTH = -1
DEATH = 1
MIN_AGE = 18
MAX_AGE = 80


def get_years(birth_date: Tuple[int, int, int], death_date: Tuple[int, int, int]) -> int:
    """
    Функция которая определяет полное количество лет.
        Параметры:
            :param birth_date: дата рождения (год, месяц, день)
            :type birth_date: Tuple[int, int, int]
            :param death_date: дата смерти (год, месяц, день)
            :type death_date: Tuple[int, int, int]
        Возвращаемое значение:
            :return: полное количество лет
            :rtype: int
    """
    number_of_years = death_date[0] - birth_date[0]
    if death_date[1] < birth_date[1]:
        number_of_years -= 1
    elif death_date[1] == birth_date[1] and death_date[2] < birth_date[2]:
        number_of_years -= 1

    return number_of_years


def find_contemporaries_sets(events: List[Tuple[Tuple[int, int, int], int, int]]) -> List[Set[int]]:
    """
    Функция которая максимальные множества современников.
        Параметры:
            :param events: список событий в котором дата события (год, месяц, день), тип события, индекс человека
            :type events: List[Tuple[Tuple[int, int, int], int, int]]
        Возвращаемое значение:
            :return: список максимальных множеств современников
            :rtype: List[Set[int]
    """
    peoples = {}
    results = []
    for event in events:
        if event[1] == BIRTH:
            peoples[event[-1]] = event[0]
        elif event[1] == DEATH:
            cur_result = set()
            for people_index, people_date in peoples.items():
                number_of_years = get_years(people_date, event[0])
                if MIN_AGE <= number_of_years <= MAX_AGE:
                    cur_result.add(people_index)
            peoples.pop(event[-1])
            if not results or not cur_result.issubset(results[-1]):
                results.append(cur_result)

    return results


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    events = []
    for index in range(1, n + 1):
        birth_day, birth_month, birth_year, death_day, death_month, death_year = map(int, input().split())
        birth_date = birth_year, birth_month, birth_day
        death_date = death_year, death_month, death_day
        number_of_years = get_years(birth_date, death_date)
        if number_of_years >= MAX_AGE:
            death_date = birth_year + MAX_AGE, birth_month, birth_day
        new_death_date = datetime.date(*death_date) - datetime.timedelta(days=1)
        death_date = new_death_date.year, new_death_date.month, new_death_date.day

        if number_of_years >= MIN_AGE:
            events.append((birth_date, BIRTH, index))
            events.append((death_date, DEATH, index))

    events.sort()
    results = find_contemporaries_sets(events)
    if results:
        for result in results:
            print(*result)
    else:
        print(0)


if __name__ == '__main__':
    main()
