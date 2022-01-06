from typing import List


def find(root: List, x: int):
    """
    Функция которая ищет значение x в бинарном дереве.

    :param root: корень относительно которого необходимо искать значение
    :type root: List
    :param x: искомое значение
    :type x: int
    """
    if not root:
        print("NO")
        return
    key = root[0]
    if key == x:
        print("YES")
        return
    elif x < key:
        left = root[1]
        if not left:
            print("NO")
            return
        else:
            return find(left, x)
    elif x > key:
        right = root[2]
        if not right:
            print("NO")
            return
        else:
            return find(right, x)


def add(root: List, x: int):
    """
    Функция которая добавляет значение x в бинарное дерево, если его в нем еще нет.

    :param root: корень относительно которого необходимо добавлять
    :type root: List
    :param x: добавляемое значение
    :type x: int
    """
    if not root:
        root.extend([x, None, None])
        print("DONE")
        return
    key = root[0]
    if key == x:
        print("ALREADY")
    if x < key:
        left = root[1]
        if not left:
            root[1] = [x, None, None]
            print("DONE")
        else:
            add(left, x)
    elif x > key:
        right = root[2]
        if not right:
            root[2] = [x, None, None]
            print("DONE")
        else:
            add(right, x)


def print_tree(root: List, depth=0):
    """
    Функция которая печатает бинарное дерево.

    :param root: корень относительно которого необходимо добавлять
    :type root: List
    :param depth: глубина рекурсии
    :type depth: int
    """
    if not root:
        return
    if root[1]:
        print_tree(root[1], depth + 1)
    print(f"{'.' * depth}{root[0]}")
    if root[2]:
        print_tree(root[2], depth + 1)


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    bin_tree = []

    with open("input.txt", "r") as file:
        number = None
        for line in file:
            line = line.split()
            if len(line) == 1:
                command = line[0]
                number = None
            elif len(line) == 2:
                command = line[0]
                number = int(line[1])

            if command == 'ADD':
                add(bin_tree, number)

            if command == 'SEARCH':
                find(bin_tree, number)

            if command == 'PRINTTREE':
                print_tree(bin_tree)


if __name__ == '__main__':
    main()
