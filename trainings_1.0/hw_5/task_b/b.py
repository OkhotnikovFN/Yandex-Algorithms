from typing import List


def get_count_cars_sets(cars_count: int, number: int, cars_list: List[int]) -> int:
    """
    Функция которая определяет количество наборов машин сумма номеров которых равна number.

    :param cars_count: количество машин
    :type cars_count: int
    :param number: счастливое число
    :type number: int
    :param cars_list: список машин
    :type cars_list: List[int]

    :return: количество наборов машин сумма номеров которых равна number
    :rtype: int
    """
    cars_list_sum = [0]
    sum_elem = 0
    for val in cars_list:
        sum_elem += val
        cars_list_sum.append(sum_elem)

    result = 0
    index = 0
    for start_index in range(cars_count):
        for end_index in range(index, cars_count + 1):
            sum_numbers = cars_list_sum[end_index] - cars_list_sum[start_index]
            if sum_numbers == number:
                result += 1
                index = end_index + 1
                break
            elif sum_numbers > number:
                index = end_index
                break
            else:
                index = end_index

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    cars_count, number = map(int, input().split())
    cars_list = list(map(int, input().split()))
    print(get_count_cars_sets(cars_count, number, cars_list))


if __name__ == '__main__':
    main()
