def determine_temperature(mode, t_room, t_cond):
    """Функция определения температуры в комнате"""
    if mode == 'auto' or (mode == 'heat' and t_room < t_cond) or (mode == 'freeze' and t_room > t_cond):
        return t_cond
    else:
        return t_room


def main():
    """Основная функция для чтения входных данных и вывода результата"""
    t_room, t_cond = map(int, input().split())
    operating_mode = input()
    print(determine_temperature(operating_mode, t_room, t_cond))


if __name__ == '__main__':
    main()
