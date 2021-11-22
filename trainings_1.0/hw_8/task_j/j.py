from typing import List, Tuple


class GenealogicalTreeNode:
    """
    Узел генеалогического дерева.
    """
    def __init__(self, name):
        self.name = name
        self.children = []
        self.depth = 0

    def update_depth(self, increment) -> None:
        """
        Функция которая обновляет глубину узла и своих потомков.

        :param increment: значение, на которое необходимо увеличить глубину
        :type increment: List[List[str]

        :return: None
        """
        self.depth += increment
        for child in self.children:
            child.update_depth(increment)


def get_nodes_depth(input_list: List[List[str]]) -> List[Tuple[str, int]]:
    """
    Функция которая находит количество всех потомков для родителя.

    :param input_list: последовательность пар значений (имя потомка, имя родителя)
    :type input_list: List[List[str]

    :return: список с парами значений (имя, количество потомков)
    :rtype: bool
    """
    family_tree = {}
    for descendant, parent in input_list:
        if parent not in family_tree:
            family_tree[parent] = GenealogicalTreeNode(parent)
        if descendant not in family_tree:
            family_tree[descendant] = GenealogicalTreeNode(descendant)

        family_tree[parent].children.append(family_tree[descendant])
        family_tree[descendant].update_depth(family_tree[parent].depth + 1)

    return sorted((name, node.depth) for name, node in family_tree.items())


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    input_list = []
    for _ in range(n - 1):
        input_list.append(input().split())
    results = get_nodes_depth(input_list)

    for name, depth in results:
        print(name, depth)


if __name__ == '__main__':
    main()
