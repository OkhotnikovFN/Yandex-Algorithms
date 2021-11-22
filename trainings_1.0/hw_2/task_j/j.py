from typing import List, Tuple


LEFT_BOUND = 30
RIGHT_BOUND = 4000
CLOSER = 'closer'


def find_frequency_bounds(first_freq: float, freq_list: List[Tuple[float, str]]) -> Tuple[int, int]:
    """
    Функция определяет, в каком интервале может находиться частота звучания треугольника.

    :param first_freq: первая частота
    :type first_freq: float
    :param freq_list: список оставшихся частот, с пометкой ближе или дальше частота звучания тюнера
    к частоте звучания треугольника по сравнению с предыдущей частотой
    :type freq_list: List[Tuple[float, str]

    :return: tuple с нижней и верхней границами звучания треугольника
    :rtype: Tuple[int, int]
    """
    freq_min = LEFT_BOUND
    freq_max = RIGHT_BOUND
    prev_freq = first_freq

    for cur_freq, condition in freq_list:
        if cur_freq != prev_freq:
            if condition == CLOSER:
                if cur_freq > prev_freq:
                    freq_min = max(freq_min, (cur_freq + prev_freq) / 2)
                else:
                    freq_max = min(freq_max, (cur_freq + prev_freq) / 2)
            else:
                if cur_freq < prev_freq:
                    freq_min = max(freq_min, (cur_freq + prev_freq) / 2)
                else:
                    freq_max = min(freq_max, (cur_freq + prev_freq) / 2)
            prev_freq = cur_freq

    return freq_min, freq_max


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    first_freq = float(input())
    freq_list = []
    for i in range(n - 1):
        freq, condition = input().split()
        freq = float(freq)
        freq_list.append((freq, condition))

    result = find_frequency_bounds(first_freq, freq_list)
    print(f'{result[0]:.6f} {result[1]:.6f}')


if __name__ == '__main__':
    main()
