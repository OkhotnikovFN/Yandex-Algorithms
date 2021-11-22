from typing import List


def find_broken_keys(key_limit: List[int], pushed_keys: List[int]) -> List[str]:
    """
    Функция которая вычисляет какие клавиши сломались.

    :param key_limit: список чисел, которые обозначают максимально возможное нажатие i-ой клавиши без поломки
    :type key_limit: List[int]
    :param pushed_keys: список нажатых клавиш
    :type pushed_keys: List[int]

    :return: список со строковым представлением, сломалась i-ая клавиша или нет
    :rtype: List[str]
    """
    keys_limit_dict = dict((index + 1, val) for index, val in enumerate(key_limit))
    for i in pushed_keys:
        keys_limit_dict[i] -= 1

    result = []
    for i in range(1, len(key_limit) + 1):
        if keys_limit_dict[i] < 0:
            result.append('YES')
        else:
            result.append("NO")

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    list_n = list(map(int, input().split()))
    k = int(input())
    list_k = list(map(int, input().split()))

    results = find_broken_keys(list_n, list_k)
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
