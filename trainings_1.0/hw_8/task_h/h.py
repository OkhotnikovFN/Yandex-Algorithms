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
        self.right_sub_tree_height = 0
        self.left_sub_tree_height = 0


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
        Функция, которая получает или устанавливает потомка для узла дерева tree_node.

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

    def check_avl_balance(self) -> bool:
        """
        Функция, которая определяет является ли дерево АВЛ-сбалансированным.

        :return: список элементов, у которых только один потомок
        :rtype: List[int]
        """
        is_avl = True
        for node in self._get_all_elements(self.root)[0]:
            is_avl = is_avl and abs(node.left_sub_tree_height - node.right_sub_tree_height) <= 1
            if not is_avl:
                break

        return is_avl

    def _get_all_elements(self, node: TreeNode, cur_height=0,
                          elements: Union[List[TreeNode], None] = None) -> Tuple[List[TreeNode], int]:
        """
        Функция, которая рекурсивно обходит дерево и выводит список элементов в порядке возрастания.

        :param node: обследуемый узел дерева
        :type node: TreeNode
        :param elements: список элементов
        :type elements: Union[List[TreeNode], None]

        :return: список элементов в порядке возрастания, текущую глубину поддерева
        :rtype: List[TreeNode]
        """
        if elements is None:
            elements = []

        if node.left:
            cur_height = self._get_all_elements(node.left, cur_height, elements)[1]
            node.left_sub_tree_height = cur_height
        elements.append(node)
        if node.right:
            cur_height = self._get_all_elements(node.right, cur_height, elements)[1]
            node.right_sub_tree_height = cur_height
        cur_height = max(node.right_sub_tree_height, node.left_sub_tree_height) + 1

        return elements, cur_height


def check_tree_avl_balance(input_list: List[int]) -> Tuple[BinTree, bool]:
    """
    Функция которая определяет является ли дерево АВЛ-сбалансированным.

    :param input_list: последовательность чисел из которых необходимо построить дерево
    :type input_list: List[int]

    :return: сущность дерева и булево представление того, является ли дерево АВЛ-сбалансированным
    :rtype: bool
    """
    bin_tree = BinTree()
    for num in input_list[:-1]:
        bin_tree.add_node(num)

    return bin_tree, bin_tree.check_avl_balance()


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    input_list = list(map(int, input().split()))
    if check_tree_avl_balance(input_list)[1]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
