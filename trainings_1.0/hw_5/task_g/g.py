from typing import Iterator


def get_count_possible_variations(max_diff: int, cards: Iterator) -> int:
    """
    Функция которая определяет количество различных вариантов счета, которые можно показать на табло.
        Параметры:
            :param max_diff: коэффициент максимального различия баллов
            :type max_diff: int
            :param cards: итератор значений чисел на карточках
            :type cards: Iterator
        Возвращаемое значение:
            :return: количество возможных вариантов
            :rtype: int
    """
    cards_dict = {}
    uniq_cards = []
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            uniq_cards.append(card)
            cards_dict[card] = 1
    uniq_cards.sort()

    right = 0
    ans = 0
    duplicates = 0
    for left in range(len(uniq_cards)):
        while right < len(uniq_cards) and uniq_cards[left] * max_diff >= uniq_cards[right]:
            if cards_dict[uniq_cards[right]] >= 2:
                duplicates += 1
            right += 1
        range_len = right - left
        if cards_dict[uniq_cards[left]] >= 2:
            ans += (range_len - 1) * 3
            duplicates -= 1
        if cards_dict[uniq_cards[left]] >= 3:
            ans += 1
        ans += (range_len - 1) * (range_len - 2) * 3
        ans += duplicates * 3

    return ans


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n, diff = map(int, input().split())
    cards = map(int, input().split())
    print(get_count_possible_variations(diff, cards))


if __name__ == '__main__':
    main()
