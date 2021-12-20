def get_min_stations(stations_count: int, boarding_station: int, landing_station: int) -> int:
    """
    Функция которая вычисляет наименьшее количество станций, которое необходимо проехать.

    :param stations_count: общее количество станций
    :type stations_count: int
    :param boarding_station: номер станции посадки
    :type boarding_station: int
    :param landing_station: номер станции высадки
    :type landing_station: int

    :return: минимальное количество промежуточных станций
    :rtype: int
    """
    min_num = min(boarding_station, landing_station)
    max_num = max(boarding_station, landing_station)
    return min(min_num + stations_count - max_num - 1, abs(boarding_station - landing_station) - 1)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N, i, j = map(int, input().split())
    print(get_min_stations(N, i, j))


if __name__ == '__main__':
    main()
