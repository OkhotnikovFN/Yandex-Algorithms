from typing import List, Tuple


def get_colors_count(n: int) -> List[Tuple[int, int]]:
    """
    Функция которая вычисляет номера цветов и сумму всех чисел данного цвета.

    :param n: количество посылок
    :type n: int

    :return: отсортированный список (номер цвета, сумма всех чисел данного цвета)
    :rtype: List[Tuple[int, int]]
    """
    packages = {}
    for _ in range(n):
        d, a = map(int, input().split())
        if d not in packages:
            packages[d] = int(a)
        else:
            packages[d] += int(a)

    result = []
    for key in sorted(list(packages)):
        result.append((key, packages[key]))

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    result = get_colors_count(n)
    for value in result:
        print(*value)


if __name__ == '__main__':
    main()
