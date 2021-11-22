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
        self.root = TreeNode(None)

    @property
    def tree_height(self):
        return max(self.root.left_sub_tree_height, self.root.right_sub_tree_height) + 1

    def add_node(self, new_value: int) -> TreeNode:
        """
        Функция, которая добавляет новый узел в бинарное дерево.

        :param new_value: добавляемое значение
        :type new_value: int

        :return: сущность нового узла
        :rtype: int
        """
        result = self._add_node(self.root, new_value)
        return result

    def _add_node(self, cur_root: TreeNode, new_value: int) -> TreeNode:
        """
        Функция, которая рекурсивно добавляет новый узел в бинарное дерево.

        :param cur_root: обследуемый узел
        :type cur_root: TreeNode
        :param new_value: добавляемое значение
        :type new_value: int

        :return: сущность нового узла
        :rtype: int
        """
        if cur_root.value is None:
            cur_root.value = new_value
            return cur_root

        if new_value == cur_root.value:
            return cur_root

        if new_value < cur_root.value:
            if cur_root.left:
                result = self._add_node(cur_root.left, new_value)
                cur_root.left_sub_tree_height = max(cur_root.left.left_sub_tree_height,
                                                    cur_root.left.right_sub_tree_height) + 1
                return result
            cur_root.left_sub_tree_height = 1
            cur_root.left = TreeNode(new_value)
            cur_root.left.parent = cur_root
            return cur_root.left

        if new_value > cur_root.value:
            if cur_root.right:
                result = self._add_node(cur_root.right, new_value)
                cur_root.right_sub_tree_height = max(cur_root.right.left_sub_tree_height,
                                                     cur_root.right.right_sub_tree_height) + 1
                return result
            cur_root.right_sub_tree_height = 1
            cur_root.right = TreeNode(new_value)
            cur_root.right.parent = cur_root
            return cur_root.right

    def check_avl_balance(self) -> bool:
        """
        Функция, которая определяет является ли дерево АВЛ-сбалансированным.

        :return: список элементов, у которых только один потомок
        :rtype: List[int]
        """
        is_avl = True
        for node in self._get_all_elements(self.root):
            is_avl = is_avl and abs(node.left_sub_tree_height - node.right_sub_tree_height) <= 1
            if not is_avl:
                break

        return is_avl

    def _get_all_elements(self, node: TreeNode, elements: Union[List[TreeNode], None] = None) -> List[TreeNode]:
        """
        Функция, которая рекурсивно обходит дерево и выводит список элементов в порядке возрастания.

        :param node: обследуемый узел дерева
        :type node: TreeNode
        :param elements: список элементов
        :type elements: Union[List[TreeNode], None]

        :return: список элементов в порядке возрастания
        :rtype: List[TreeNode]
        """
        if elements is None:
            elements = []
        if node.left:
            self._get_all_elements(node.left, elements)
        elements.append(node)
        if node.right:
            self._get_all_elements(node.right, elements)

        return elements


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
