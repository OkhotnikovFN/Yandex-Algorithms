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
        self.node_height = 0


class BinTree:
    """
    Бинарное дерево.
    """
    def __init__(self):
        self.tree_height = 0
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

    def add_node(self, new_value: int) -> Tuple[TreeNode, bool]:
        """
        Функция, которая добавляет новый узел в бинарное дерево и вычисляет новую получившуюся высоту.

        :param new_value: добавляемое значение
        :type new_value: int

        :return: сущность нового узла и флаг добавления узла в дерево
        :rtype: int
        """
        add_flag = True
        new_node = TreeNode(None)
        cur_root = self.root
        cur_height = 1
        while cur_root.value:
            if new_value < cur_root.value:
                cur_root = self.get_or_set_node_child(cur_root, new_node)
            elif new_value > cur_root.value:
                cur_root = self.get_or_set_node_child(cur_root, new_node, False)
            else:
                add_flag = False
                break
            cur_height += 1

        cur_root.value = new_value
        cur_root.node_height = cur_height
        self.tree_height = max(self.tree_height, cur_height)

        return cur_root, add_flag

    def find_max_value(self) -> int:
        """
        Функция, которая вычисляет максимальное значение в дереве.

        :return: максимальное значение в дереве
        :rtype: int
        """
        cur_root = self.root

        max_value = cur_root.value
        while cur_root:
            if not cur_root.right:
                max_value = cur_root.value

            cur_root = cur_root.right

        return max_value

    def find_second_max(self) -> int:
        """
        Функция, которая вычисляет второе по величине значение в дереве.

        :return: второе по величине значение в дереве
        :rtype: int
        """
        return self._find_second_max(self.root)

    def _find_second_max(self, node: TreeNode, went_left_once: bool = False) -> int:
        """
        Функция, которая рекурсивно вычисляет второе по величине значение в дереве.

        :param node: обследуемый узел
        :type node: TreeNode
        :param went_left_once: флаг, который обозначает единственный переход в левого ребенка
        :type went_left_once: bool

        :return: второе по величине значение в дереве
        :rtype: int
        """
        if node.right:
            return self._find_second_max(node.right, went_left_once)
        if node.left and not went_left_once:
            return self._find_second_max(node.left, True)
        return node.value if went_left_once else node.parent.value


def find_second_max_in_tree(input_list: List[int]) -> Tuple[BinTree, int]:
    """
    Функция которая находит второй по величине элемент в бинарном дереве.

    :param input_list: последовательность чисел из которых необходимо построить дерево
    :type input_list: List[int]

    :return: сущность дерева и второй по величине элемент
    :rtype: int
    """
    bin_tree = BinTree()
    for num in input_list[:-1]:
        bin_tree.add_node(num)

    return bin_tree, bin_tree.find_second_max()


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    input_list = list(map(int, input().split()))
    print(find_second_max_in_tree(input_list)[1])


if __name__ == '__main__':
    main()
