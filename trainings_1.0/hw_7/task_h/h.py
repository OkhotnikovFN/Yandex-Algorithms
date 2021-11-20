from typing import List


BEGIN_PROTECT = -1
END_PROTECT = 1
START_POSITION = 0
END_POSITION = 10000


def my_func(input_params: List[int]) -> str:
    """
    Функция которая проверяет подходят ли данные охранники под условия задачи.
        Параметры:
            :param input_params: список, первым элементом которого является число охранников,
            за которым следуют пары неотрицательных целых чисел — время прихода на дежурство и ухода
            :type : List[int]
        Возвращаемое значение:
            :return: строковое представление соответствия условию задачи
            :rtype: str
    """
    guards_count = input_params[0]
    events = []
    for i in range(guards_count):
        a, b = input_params[2 * i + 1], input_params[2 * i + 2]
        events.append((a, BEGIN_PROTECT, i))
        events.append((b, END_PROTECT, i))
    events.sort()

    good_guards = set()
    now_guards = set()
    good_flag = True
    prev_time = -1
    for event in events:
        if event[0] != 0 and len(now_guards) == 0:
            good_flag = False
            break
        if len(now_guards) == 1 and event[0] != prev_time:
            good_guards.update(now_guards)
        if event[1] == BEGIN_PROTECT:
            now_guards.add(event[2])
        elif event[1] == END_PROTECT:
            now_guards.remove(event[2])
        prev_time = event[0]

    if events[-1][0] != END_POSITION:
        good_flag = False
    if good_flag and len(good_guards) == guards_count:
        return 'Accepted'
    else:
        return 'Wrong Answer'


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    k = int(input())
    for _ in range(k):
        input_string = list(map(int, input().split()))
        print(my_func(input_string))


if __name__ == '__main__':
    main()
