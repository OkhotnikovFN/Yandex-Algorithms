from typing import List


def walk(tree_root: List, res: List, path: str = ''):
    """
    Рекурсивная функцию обхода дерева в глубину
    (по дороге строим текущий путь, который добавляем к результатам при достижении листа дерева).

    :param tree_root: корень относительно которого строить дерево
    :type tree_root: List
    :param res: результат
    :type res: List
    :param path: код листа
    :type path: str
    """
    if tree_root[0]:
        walk(tree_root[0], res, f"{path}{0}")
    if tree_root[1]:
        walk(tree_root[1], res, f"{path}{1}")
    if not tree_root[0] and not tree_root[1]:
        res.append(f"{path}\n")


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    with open('input.txt') as file:
        lines = file.readlines()

    outfile = open('output.txt', 'w')

    # Идем по кодам деревьев и разворачиваем их в сами деревья
    # по правилам, указанным в условии задачи:
    for input_line in lines[1:]:
        commands = [char for char in input_line]

        # Формат узла: [left_subtree, right_subtree, parent, child_type]
        # Тип потомка (child_type): -1 для левого, 1 - для правого.
        tree = [[[], [], None, 0]]
        root = tree[0]
        current = root

        for command in commands:
            if command == 'D':
                new_elem = [[], [], current, -1]
                current[0] = new_elem
                current = new_elem
            elif command == 'U':
                while current[3] == 1:
                    current = current[2]
                current = current[2]
                new_elem = [[], [], current, 1]
                current[1] = new_elem
                current = new_elem

        tree = tree[0]

        # Для каждого построенного дерева совершаем обход и выводим результаты:
        results = []
        walk(tree, results)
        outfile.write(f"{len(results)}\n")
        outfile.writelines(results)

    outfile.close()


if __name__ == '__main__':
    main()
