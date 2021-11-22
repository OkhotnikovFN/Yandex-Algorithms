def get_count_operations(k: int, operations: str) -> int:
    """
    Функция которая определяет количество экономически целесообразных способов использования робота.

    :param k: количество операций, которые можно записать в память робота
    :type k: int
    :param operations: список операций в виде строки
    :type operations: str

    :return: количество экономически целесообразных способов использования робота
    :rtype: int
    """
    result = 0
    successful_operations_count = 0
    for right in range(k, len(operations)):
        if operations[right] == operations[right - k]:
            successful_operations_count += 1
            result += successful_operations_count
        else:
            successful_operations_count = 0

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    k = int(input())
    operations = input()
    print(get_count_operations(k, operations))


if __name__ == '__main__':
    main()
