def get_desk_side(width: int, height: int, diploma_count: int) -> int:
    """
    Функция вычисления минимального размера стороны квадратной доски.

    :param width: ширина диплома
    :type width: int
    :param height: высота диплома
    :type height: int
    :param diploma_count: количество дипломов
    :type diploma_count: int

    :return: минимальный размер стороны квадратной доски
    :rtype: int
    """
    left = max(width, height)
    right = left * diploma_count
    while right - left > 1:
        middle = (right + left) // 2
        possible_diploma_count = (middle // width) * (middle // height)
        if possible_diploma_count < diploma_count:
            left = middle
        else:
            right = middle
    return right


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    w, h, n = map(int, input().split())
    print(get_desk_side(w, h, n))


if __name__ == '__main__':
    main()
