from typing import List


def get_count_possible_ways(n: int, r: int, monuments: List[int]) -> int:
    """
    Функция которая вычисляет количество способов выбрать два различных памятника для организации свиданий.
        Параметры:
            :param n: количество памятников
            :type n: int
            :param r: минимальное расстояние видимости
            :type r: int
            :param monuments: список расстояний от i-го памятника до начала улицы
            :type monuments: List[int]
        Возвращаемое значение:
            :return: количество возможных способов
            :rtype: int
    """
    result = 0
    start = 0
    for monument in monuments:
        for index in range(start, n):
            if monuments[index] - monument > r:
                result += n - index
                start = index
                break
            start = index

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, r = map(int, input().split())
    monuments = list(map(int, input().split()))
    print(get_count_possible_ways(n, r, monuments))


if __name__ == '__main__':
    main()
