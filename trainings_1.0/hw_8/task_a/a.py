from typing import List, Tuple, Union


class TreeNode:
    """
    Узел бинарного дерева.
    """

    def __init__(self, value: Union[int, None]):
        """
        Инициализация нового узла, которому присваивается значение value, но отсутствует информация о родителе
        и отсутствуют потомки.

        :param value: значение узла дерева
        :type value: Union[int, None]
        """
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BinTree:
    """
    Бинарное дерево.
    """

    def __init__(self):
        self.height = 0
        self.root = TreeNode(None)

    @staticmethod
    def get_or_set_node_child(tree_node: TreeNode, new_node: TreeNode, is_left_child: bool = True) -> TreeNode:
        """
        Функция, которая получает или устанавливает левого потомка для узла дерева tree_node.

        :param tree_node: узел дерева
        :type tree_node: TreeNode
        :param new_node: новый левый потомок
        :type new_node: TreeNode
        :param is_left_child: булево значение, является ли потомок левым
        :type is_left_child: bool

        :return: текущий левый потомок узла дерева tree_node
        :rtype: TreeNode
        """
        if is_left_child:
            node_child = tree_node.left
        else:
            node_child = tree_node.right

        if node_child is None:
            if is_left_child:
                tree_node.left = new_node
            else:
                tree_node.right = new_node
            new_node.parent = tree_node
        else:
            new_node = node_child

        return new_node

    def add_node(self, new_value: int) -> Tuple[TreeNode, int]:
        """
        Функция, которая добавляет новый узел в бинарное дерево и вычисляет новую получившуюся высоту.

        :param new_value: добавляемое значение
        :type new_value: int

        :return: сущность нового узла и высоту получившегося дерева
        :rtype: int
        """
        new_node = TreeNode(None)
        cur_root = self.root
        cur_height = 1
        while cur_root.value:
            if new_value < cur_root.value:
                cur_root = self.get_or_set_node_child(cur_root, new_node)
            elif new_value > cur_root.value:
                cur_root = self.get_or_set_node_child(cur_root, new_node, False)
            else:
                break
            cur_height += 1

        cur_root.value = new_value
        self.height = max(self.height, cur_height)

        return cur_root, self.height


def get_tree_height(input_list: List[int]) -> Tuple[BinTree, int]:
    """
    Функция которая заполняет бинарное дерево и выводит сущность дерева и его высоту.

    :param input_list: последовательность чисел из которых необходимо построить дерево
    :type input_list: List[int]

    :return: сущность дерева и его высота
    :rtype: int
    """
    bin_tree = BinTree()
    for num in input_list[:-1]:
        bin_tree.add_node(num)

    return bin_tree, bin_tree.height


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    input_list = list(map(int, input().split()))
    print(get_tree_height(input_list)[1])


if __name__ == '__main__':
    main()
