from typing import List


def find_min_time(number_of_folders: int, folder_list: List[int]) -> int:
    """
    Функция которая определяет минимальное количество секунд,
    необходимое Ивану в худшем случае для определения того, в какой папке содержится диплом.

    :param number_of_folders: количество папок
    :type number_of_folders: int
    :param folder_list: список количества дипломов, в каждой из папок
    :type folder_list: List[int]

    :return: минимальное количество секунд
    :rtype: int
    """
    if number_of_folders == 1:
        return 0

    folder_list.sort()
    return sum(folder_list[:-1])


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    folder_list = list(map(int, input().split()))
    print(find_min_time(n, folder_list))


if __name__ == '__main__':
    main()
