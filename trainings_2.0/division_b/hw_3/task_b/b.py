from typing import List


def check_occurrence(nums_list: List[str]) -> List[str]:
    """
    Функция которая определяет, было ли уже число в списке.

    :param nums_list: исходный список чисел
    :type nums_list: List[str]

    :return: список с ответами
    :rtype: List[str]
    """
    nums_set = set()
    result = []
    for num in nums_list:
        if num in nums_set:
            result.append("YES")
        else:
            result.append("NO")
            nums_set.add(num)

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    nums_list = input().split()
    print(*check_occurrence(nums_list), sep='\n')


if __name__ == '__main__':
    main()
