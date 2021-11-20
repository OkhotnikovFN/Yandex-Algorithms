ARRIVAL = -1
DEPARTURE = 1


def make_minutes(time) -> int:
    """
    Функция которая переводит часы и минуты в минуты.
        Параметры:
            :param time: строковое представление времени (hh:mm)
            :type time: str
        Возвращаемое значение:
            :return: количество минут в данном интервале времени
            :rtype: int
    """
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)


def get_required_busses_count(cities_count: int, routes_count: int) -> int:
    """
    Функция которая вычисляет минимально необходимое количество автобусов.
        Параметры:
            :param cities_count: количество городов
            :type cities_count: int
            :param routes_count: количество автобусных рейсов
            :type routes_count:int
        Возвращаемое значение:
            :return: минимально необходимое количество автобусов
            :rtype: int
    """
    buses_count = [0] * (cities_count + 1)
    buses_balance = [0] * (cities_count + 1)
    events = []
    over_night = 0
    for i in range(routes_count):
        city_departure, departure_time, city_arrival, arrival_time = input().split()
        city_departure = int(city_departure)
        city_arrival = int(city_arrival)
        departure_time = make_minutes(departure_time)
        arrival_time = make_minutes(arrival_time)
        if arrival_time < departure_time:
            over_night += 1
        buses_balance[city_departure] -= 1
        buses_balance[city_arrival] += 1
        events.append((arrival_time, ARRIVAL, city_arrival))
        events.append((departure_time, DEPARTURE, city_departure))

    disbalance = False
    for i in range(cities_count + 1):
        if buses_balance[i] != 0:
            disbalance = True
    if disbalance:
        return -1

    events.sort()
    for event in events:
        if event[1] == ARRIVAL:
            buses_count[event[2]] += 1
        elif event[1] == DEPARTURE:
            if buses_count[event[2]] > 0:
                buses_count[event[2]] -= 1
    ans = 0
    for i in range(cities_count + 1):
        ans += buses_count[i]
    return ans + over_night


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, m = map(int, input().split())
    print(get_required_busses_count(n, m))


if __name__ == '__main__':
    main()
