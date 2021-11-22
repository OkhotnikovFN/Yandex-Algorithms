def check_genome_matching(genome_1: str, genome_2: str) -> int:
    """
    Функция которая проверяет степень близости genome_1 к genome_2.

    :param genome_1: первый геном
    :type genome_1: str
    :param genome_2: второй геном
    :type genome_2: str

    :return: степень близости genome_1 к genome_2
    :rtype: int
    """
    result = 0
    set_genome_2 = set()
    for index in range(len(genome_2) - 1):
        set_genome_2.add(genome_2[index:index + 2])

    for index in range(len(genome_1) - 1):
        if genome_1[index:index + 2] in set_genome_2:
            result += 1

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    genome_1 = input()
    genome_2 = input()
    print(check_genome_matching(genome_1, genome_2))


if __name__ == '__main__':
    main()
