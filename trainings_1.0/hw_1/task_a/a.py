def determine_temperature(mode: str, t_room: int, t_cond: int) -> int:
    """
    Функция определения температуры в комнате.
        Параметры:
            mode: режим работы кондиционера
            t_room(int): температура в комнате
            t_cond(int): температура установленная на кондиционере
        Возвращаемое значение:
            t_room_final(int): температура в комнате через час
    """
    if mode == 'auto' or (mode == 'heat' and t_room < t_cond) or (mode == 'freeze' and t_room > t_cond):
        t_room_final = t_cond
    else:
        t_room_final = t_room
    return t_room_final


def main():
    """Основная функция для чтения входных данных и вывода результата"""
    t_room, t_cond = map(int, input().split())
    operating_mode = input()
    print(determine_temperature(operating_mode, t_room, t_cond))


if __name__ == '__main__':
    main()
