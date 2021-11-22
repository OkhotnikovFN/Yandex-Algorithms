def define_details_count(n: int, k: int, m: int) -> int:
    """
    Функция которая вычисляет количество произведенных деталей.

    :param n: вес всего сплава в начале
    :type n: int
    :param k: вес одной заготовки
    :type k: int
    :param m: вес одной детали
    :type m: int

    :return: количество деталей
    :rtype: int
    """
    details_count = 0
    if m > k or k > n:
        return details_count

    while n >= k:
        workpiece_count = n // k
        detail_now = (k // m) * workpiece_count
        details_count += detail_now
        n = n % k + (k % m) * workpiece_count

    return details_count


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N, K, M = map(int, input().split())
    print(define_details_count(N, K, M))


if __name__ == '__main__':
    main()
