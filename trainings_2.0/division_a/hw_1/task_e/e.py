from typing import List, Tuple


def my_func(perimeter: int) -> List[Tuple]:
    """
    Функция которая вычисляет стороны треугольника с самой большой площадью и самой маленькой площадью.

    :param perimeter: периметр треугольника
    :type perimeter: int

    :return: два кортежа с длинами сторон, или -1 если ответа не существует
    :rtype: List[Tuple]
    """
    result = []
    max_side_1 = perimeter // 3
    max_side_2 = (perimeter - max_side_1) // 2
    max_side_3 = perimeter - max_side_1 - max_side_2

    if max_side_1 + max_side_2 <= max_side_3:
        result.append((-1,))
    else:
        result.append((max_side_1, max_side_2, max_side_3))
        if perimeter % 2 == 1:
            min_side_1 = 1
        else:
            min_side_1 = 2
        min_side_2 = (perimeter - min_side_1) // 2
        min_side_3 = perimeter - min_side_1 - min_side_2
        result.append((min_side_1, min_side_2, min_side_3))

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    p = int(input())
    result = my_func(p)
    for val in result:
        print(*val)


if __name__ == '__main__':
    main()
