from typing import Dict, Tuple, List


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


def find_parent(tree: Dict, person1: str, person2: str) -> int:
    """
    Функция которая вычисляет является ли кто-то из узлов другому родителем.

    :param tree: дерево
    :type tree: Dict
    :param person1: первый узел
    :type person1: str
    :param person2: второй узел
    :type person2: str

    :return: 1, если person1 является предком person2
    :rtype: int
    """
    pr_upper = tree[person2][0]
    if pr_upper == person1:
        return 1
    elif pr_upper == 0:
        return -1
    else:
        return find_parent(tree, person1, pr_upper)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    family_tree = dict()
    ans = []

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
            height_1 = family_tree[person1][1]
            height_2 = family_tree[person2][1]
            if height_1 < height_2:
                request = find_parent(family_tree, person1, person2)
                if request == 1:
                    ans.append(1)
                elif request == -1:
                    ans.append(0)
            elif height_1 > height_2:
                request = find_parent(family_tree, person2, person1)
                if request == 1:
                    ans.append(2)
                elif request == -1:
                    ans.append(0)
            else:
                ans.append(0)

    print(*ans)


if __name__ == '__main__':
    main()
