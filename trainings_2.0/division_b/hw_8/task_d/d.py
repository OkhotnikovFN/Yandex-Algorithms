from typing import List


def dfs(cur_index, neighbors: List, sub_size: List, visited: List) -> int:
    """
    Функция которая вычисляет максимальное количество последовательно
    соединенных бусинок присутствует в полученной фигуре.

    :param cur_index: индекс обрабатываемой бусинки
    :type cur_index: int
    :param neighbors: дерево соединенных бусинок
    :type neighbors: List
    :param sub_size: список длин для бусинок
    :type sub_size: List
    :param visited: список обработанных бусинок
    :type visited: List

    :return: максимальное количество последовательно соединенных бусинок
    :rtype: int
    """
    visited[cur_index] = True
    best = 1
    max1 = -1
    max2 = -1
    sub_size[cur_index] = 1
    for next_val in neighbors[cur_index]:
        if not visited[next_val]:
            best = max(dfs(next_val, neighbors, sub_size, visited), best)
            if sub_size[next_val] > max1:
                max2 = max1
                max1 = sub_size[next_val]
            elif sub_size[next_val] > max2:
                max2 = sub_size[next_val]
    best = max(best, max1 + 1)
    best = max(best, max1 + max2 + 1)
    sub_size[cur_index] = max(sub_size[cur_index], max1 + 1)
    return best


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())
    neighbors = []

    for _ in range(N + 1):
        neighbors.append([])

    for _ in range(N - 1):
        a, b = map(int, input().split())
        neighbors[a].append(b)
        neighbors[b].append(a)
    sub_size = [0] * (N + 1)
    visited = [False] * (N + 1)

    print(dfs(1, neighbors, sub_size, visited))


if __name__ == '__main__':
    main()
