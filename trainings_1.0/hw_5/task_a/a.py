from typing import List, Tuple


def find_best_style(undershirts: List[int], pants: List[int], pants_count: int) -> Tuple[int, int]:
    """
    Функция которая определяет лучший стиль.

    :param undershirts: список цветов маек
    :type undershirts: List[int]
    :param pants: список цветов штанов
    :type pants: List[int]
    :param pants_count: количество цветов штанов
    :type pants_count: int

    :return: цвет майки и цвет штанов
    :rtype: Tuple[int, int]
    """
    min_style = abs(undershirts[0] - pants[0])
    result = undershirts[0], pants[0]
    start_ind_pants = 0

    for undershirt in undershirts:
        for ind_pant in range(start_ind_pants, pants_count):
            style = abs(undershirt - pants[ind_pant])
            if style < min_style:
                min_style = style
                result = undershirt, pants[ind_pant]

            if undershirt > pants[ind_pant]:
                start_ind_pants = ind_pant
            else:
                break

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    undershirts_count = int(input())
    undershirts = list(map(int, input().split()))
    pants_count = int(input())
    pants = list(map(int, input().split()))
    print(*find_best_style(undershirts, pants, pants_count))


if __name__ == '__main__':
    main()
