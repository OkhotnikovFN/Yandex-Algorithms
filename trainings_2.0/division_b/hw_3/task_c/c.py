from typing import List


def find_uniq_nums(nums_list: List[str]) -> List[str]:
    """
    Функция которая находит уникальные элементы в списке.

    :param nums_list: проверяемый список
    :type nums_list: List[str]

    :return: список уникальных элементов
    :rtype: List[str]
    """
    nums_dict = {}
    for num in nums_list:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    uniq_nums = []
    for num in nums_list:
        if nums_dict[num] == 1:
            uniq_nums.append(num)

    return uniq_nums


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    nums_list = input().split()
    print(*find_uniq_nums(nums_list))


if __name__ == '__main__':
    main()
