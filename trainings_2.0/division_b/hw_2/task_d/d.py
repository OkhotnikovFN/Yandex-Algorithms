from typing import List, Tuple, Union


def get_base_coords(l: int, coord_list: List[int]) -> Union[Tuple[int, int], Tuple[int]]:
    """
    Функция которая определяет координаты ножек, которые необходимо оставить.

    :param l: Длинна лавочки
    :type l: int
    :param coord_list: координаты ножек
    :type coord_list: List[int]

    :return:
    :rtype:
    """
    middle = l // 2
    if middle in coord_list and l % 2:
        return (middle,)

    left = right = None
    for i, value in enumerate(coord_list):
        if value >= middle:
            left = coord_list[i - 1]
            right = value
            break

    return left, right


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    l, k = map(int, input().split())
    coord_list = list(map(int, input().split()))
    print(*get_base_coords(l, coord_list))


if __name__ == '__main__':
    main()
