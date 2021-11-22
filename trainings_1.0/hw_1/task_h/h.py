from typing import Union, Tuple


STOP_TIME = 1


def define_waiting_time(train_1_waiting: int, train_2_waiting: int,
                        train_1_count: int, train_2_count: int) -> Union[Tuple[int, int], int]:
    """
    Функция которая вычисляет минимальное и максимальное время в минутах, которое Таня могла стоять на платформе.

    :param train_1_waiting: интервал между поездами на первом пути
    :type train_1_waiting: int
    :param train_2_waiting: интервал между поездами на втором пути
    :type train_2_waiting: int
    :param train_1_count: количество поездов на первом пути, которые увидела Таня
    :type train_1_count: int
    :param train_2_count: количество поездов на втором пути, которые увидела Таня
    :type train_2_count: int

    :return: количество деталей
    :rtype: Union[Tuple[int, int], int]
    """
    time_1_min = train_1_count * STOP_TIME + (train_1_count - 1) * train_1_waiting
    time_1_max = train_1_count * STOP_TIME + (train_1_count + 1) * train_1_waiting
    time_2_min = train_2_count * STOP_TIME + (train_2_count - 1) * train_2_waiting
    time_2_max = train_2_count * STOP_TIME + (train_2_count + 1) * train_2_waiting
    min_time = max(time_1_min, time_2_min)
    max_time = min(time_1_max, time_2_max)
    if max_time < min_time:
        return -1
    else:
        return min_time, max_time


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a = int(input())
    b = int(input())
    n = int(input())
    m = int(input())
    result = define_waiting_time(a, b, n, m)
    if isinstance(result, tuple):
        print(*result)
    else:
        print(result)


if __name__ == '__main__':
    main()
