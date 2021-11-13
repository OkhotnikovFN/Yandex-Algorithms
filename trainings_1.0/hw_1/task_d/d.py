from typing import Union


def check_solution(a: int, b: int, c: int) -> Union[str, int]:
    """
    Функция которая проверяет есть ли целочисленные решения уравнения.
        Параметры:
            :param a: коэффициент уравнения
            :type a: int
            :param b: коэффициент уравнения
            :type b: int
            :param c: коэффициент уравнения
            :type c: int
        Возвращаемое значение:
            :return: ответ, если он имеется, или NO SOLUTION ,
            если решений нет, если решений бесконечно много - MANY SOLUTIONS.
            :rtype: Union[str, int]
    """
    if c < 0:
        answer = 'NO SOLUTION'

    elif a == 0:
        if c * c == b:
            answer = 'MANY SOLUTIONS'
        else:
            answer = 'NO SOLUTION'

    elif (c * c - b) % a == 0:
        answer = (c * c - b) // a
    else:
        answer = 'NO SOLUTION'

    return answer


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    a = int(input())
    b = int(input())
    c = int(input())
    print(check_solution(a, b, c))


if __name__ == '__main__':
    main()
