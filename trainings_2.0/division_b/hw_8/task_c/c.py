from typing import Dict, List, Tuple


def find_height(tree: Dict, parent: List, height: int) -> Tuple[int, str]:
    """
    Функция которая вычисляет высоту узла и изначального предка всех потомков.

    :param tree: дерево
    :type tree: Dict
    :param parent: родитель в дереве
    :type parent: List
    :param height: высота узла
    :type height: int

    :return: высота узла и изначальный предок
    :rtype: Tuple[int, str]
    """
    ancestor = None
    if parent[0] in tree:
        parent_upper = tree[parent[0]]
        height += 1
        return find_height(tree, parent_upper, height)
    else:
        if height == 1:
            ancestor = parent[0]
        return height, ancestor


def find_parent(tree, person_1, person_2) -> str:
    """
    Функция которая вычисляет наименьшего общего предка данных элементов.

    :param tree: дерево
    :type tree: Dict
    :param person_1: первый узел
    :type person_1: str
    :param person_2: второй узел
    :type person_2: str

    :return: наименьший общий предок
    :rtype: str
    """
    par_1 = tree[person_1][0]
    par_1_set = {person_1, par_1}
    par_2 = tree[person_2][0]

    while par_1:
        par_1 = tree[par_1][0]
        par_1_set.add(par_1)

    if person_2 in par_1_set:
        return person_2
    if par_2 in par_1_set:
        return par_2

    while True:
        par_2 = tree[par_2][0]
        if par_2 in par_1_set:
            return par_2


def main():
    """Основная функция для чтения входных данных и вывода результата."""

    family_tree = dict()

    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        for line in range(n - 1):
            child, parent = file.readline().split()
            family_tree[child] = [parent]

        for child, parent in family_tree.items():
            height, ancestor = find_height(family_tree, parent, 1)
            family_tree[child].extend([height])
            if ancestor is not None:
                main_parent = ancestor
        family_tree[main_parent] = [0, 0]

        for line in file:
            person1, person2 = line.split()
            result = find_parent(family_tree, person1, person2)
            print(result)


if __name__ == '__main__':
    main()
