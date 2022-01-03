from typing import List


HOUSE = 1
SHOP = 2
OFFICE = 0


def get_max_length(building_list: List[int]) -> int:
    """
    Функция которая определяет наибольшее расстояние, которое приходится преодолевать жителям Нового проспекта,
    чтобы дойти от своего дома до ближайшего магазина.

    :param building_list: список идентификаторов зданий
    :type building_list: List[int]

    :return: наибольшее расстояние
    :rtype: int
    """

    coord_dict = {}
    for index, value in enumerate(building_list):
        if value in coord_dict:
            coord_dict[value].append(index)
        else:
            coord_dict[value] = [index]

    distances_list = []
    for house_coord in coord_dict[HOUSE]:
        min_distance = float('inf')
        for shop_coord in coord_dict[SHOP]:
            min_distance = min(min_distance, abs(house_coord - shop_coord))
        distances_list.append(min_distance)

    return max(distances_list)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    building_list = list(map(int, input().split()))
    print(get_max_length(building_list))


if __name__ == '__main__':
    main()
