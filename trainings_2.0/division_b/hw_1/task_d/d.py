from typing import List


def my_func(coord: List[int], n_count: int) -> int:
    """
    Функция которая определяет лучшее положение школы.

    :param coord: список координат домов
    :type coord: List[int]
    :param n_count: количество домов
    :type n_count: int

    :return: координаты школы
    :rtype int:
    """
    if n_count % 2:
        return coord[n_count // 2]
    return round((coord[n_count // 2] + coord[n_count // 2 - 1]) / 2)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())
    coord = list(map(int, input().split()))
    print(my_func(coord, N))


if __name__ == '__main__':
    main()
