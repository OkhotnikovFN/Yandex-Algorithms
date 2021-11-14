from typing import List, Tuple


def draw_minefield(rows_count: int, columns_count: int, coord_list: List[Tuple[int, int]]) -> str:
    """
    Функция которая рисует минное поле по заданным размерам поля и координатам мин.
        Параметры:
            :param rows_count: количество рядов в минном поле
            :type rows_count: int
            :param columns_count: количество столбцов в минном поле
            :type columns_count: int
            :param coord_list: координаты мин на минном поле
            :type coord_list: List[Tuple[int, int]]
        Возвращаемое значение:
            :return: строковое представление минного поля
            :rtype: str
    """
    field = []
    for _ in range(rows_count):
        field.append([0] * columns_count)

    for x, y in coord_list:
        field[x][y] = '*'
        for num_x in range(x-1, x+2):
            for num_y in range(y - 1, y + 2):
                if 0 <= num_x <= rows_count - 1 and 0 <= num_y <= columns_count - 1:
                    if field[num_x][num_y] != '*':
                        field[num_x][num_y] += 1

    field_rows = []
    for row in field:
        field_rows.append(' '.join(map(str, row)))
    result = '\n'.join(field_rows)
    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    rows_count, columns_count, mine_count = map(int, input().split())
    coord_list = []
    for _ in range(mine_count):
        p, q = map(lambda num: int(num) - 1, input().split())
        coord_list.append((p, q))
    print(draw_minefield(rows_count, columns_count, coord_list))


if __name__ == '__main__':
    main()
