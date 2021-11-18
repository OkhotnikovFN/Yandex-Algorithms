from typing import List


MAX_POWER = 1000


def find_min_cost(required_powers: List[int], conditioners: dict) -> int:
    """
    Функция которая определяет минимальную суммарную стоимость кондиционеров.
        Параметры:
            :param required_powers: список требуемых минимальных мощностей кондиционеров
            :type required_powers: List[int]
            :param conditioners: словарь, в котором ключом является мощность кондиционера, а значением - его стоимость
            :type conditioners: dict
        Возвращаемое значение:
            :return: суммарная минимальная стоимость кондиционеров
            :rtype: int
    """
    conditioners_prices = [(power, price) for power, price in conditioners.items()]
    conditioners_power_prices = [float('inf')] * (MAX_POWER + 1)

    for power, price in conditioners_prices:
        power_index = 1
        while power_index <= power:
            if price < conditioners_power_prices[power_index]:
                conditioners_power_prices[power_index] = price
            power_index += 1

    result = 0
    for power in required_powers:
        result += conditioners_power_prices[power]

    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    required_powers = list(map(int, input().split()))
    m = int(input())
    conditioners = {}

    for _ in range(m):
        power, price = map(int, input().split())
        if power in conditioners:
            if price < conditioners[power]:
                conditioners[power] = price
        else:
            conditioners[power] = price

    print(find_min_cost(required_powers, conditioners))


if __name__ == '__main__':
    main()
