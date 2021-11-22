def determine_temperature(mode: str, t_room: int, t_cond: int) -> int:
    """
    Функция определения температуры в комнате.

    :param mode: режим работы кондиционера
    :type mode: str
    :param t_room: температура в комнате
    :type t_room: int
    :param t_cond: температура установленная на кондиционере
    :type t_cond: int

    :return: температура в комнате через час
    :rtype: int
    """
    if mode == 'auto' or (mode == 'heat' and t_room < t_cond) or (mode == 'freeze' and t_room > t_cond):
        t_room_final = t_cond
    else:
        t_room_final = t_room
    return t_room_final


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    t_room, t_cond = map(int, input().split())
    operating_mode = input()
    print(determine_temperature(operating_mode, t_room, t_cond))


if __name__ == '__main__':
    main()
