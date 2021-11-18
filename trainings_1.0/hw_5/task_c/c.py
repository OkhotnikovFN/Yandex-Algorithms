from typing import List, Tuple


def define_treks(n: int, mountains: List[Tuple[int, int]]) -> Tuple[List[int], List[int]]:
    """
    Функция которая определяет два списка с высотами подъемов при движении слева и при движении справа.
        Параметры:
            :param n: количество точек ломаной, задающей горную цепь
            :type n: int
            :param mountains: список точек ломаной, задающей горную цепь
            :type mountains: List[Tuple[int, int]
        Возвращаемое значение:
            :return: два списка с высотами подъемов при движении слева и при движении справа
            :rtype: Tuple[List[int], List[int]]
    """
    mountains_left = [0]
    for i in range(1, n):
        if mountains[i][1] > mountains[i - 1][1]:
            emmit = mountains_left[i - 1] + (mountains[i][1] - mountains[i - 1][1])
        else:
            emmit = mountains_left[i - 1]
        mountains_left.append(emmit)

    mountains_right = [0]
    for i in range(1, n):
        if mountains[-i - 1][1] > mountains[-i][1]:
            emmit = mountains_right[i - 1] + (mountains[-i - 1][1] - mountains[-i][1])
        else:
            emmit = mountains_right[i - 1]
        mountains_right.append(emmit)
    return mountains_left, mountains_right


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    mountains = []
    for _ in range(n):
        x, y = map(int, input().split())
        mountains.append((x, y))

    mountains_left, mountains_right = define_treks(n, mountains)

    m = int(input())
    for _ in range(m):
        left, right = map(int, input().split())
        if left < right:
            print(mountains_left[right - 1] - mountains_left[left - 1])
        else:
            print(mountains_right[-right] - mountains_right[-left])


if __name__ == '__main__':
    main()
