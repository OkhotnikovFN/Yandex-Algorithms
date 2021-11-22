from typing import List, Tuple


class GenealogicalTreeNode:
    """
    Узел генеалогического дерева.
    """
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.descendants_count = 0

    def update_descendants_count(self, increment: int) -> None:
        """
        Функция которая обновляет количество потомков у родителя.

        :param increment: количество на сколько необходимо увеличить
        :type increment: int

        :return: None
        """
        cur_node = self
        self.descendants_count += increment
        while cur_node.parent:
            cur_node = cur_node.parent
            cur_node.descendants_count += increment


def find_descendants_count(input_list: List[List[str]]) -> List[Tuple[str, int]]:
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

        family_tree[descendant].parent = family_tree[parent]
        family_tree[parent].update_descendants_count(family_tree[descendant].descendants_count + 1)

    return sorted((name, node.descendants_count) for name, node in family_tree.items())


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    input_list = []
    for _ in range(n - 1):
        input_list.append(input().split())
    results = find_descendants_count(input_list)

    for name, descendants_count in results:
        print(name, descendants_count)


if __name__ == '__main__':
    main()
