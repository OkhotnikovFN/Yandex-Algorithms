from typing import List


NUMBERS_COUNT = 4


def check_numbers(numbers: List[str]) -> List[str]:
    """
    Функция которая сравнивает новый номер, с номерами, которые уже есть в телефоне.

    :param numbers: список всех номеров, первый номер в списке - это новый номер
    :type numbers: List[str]

    :return: список с ответами, совпадает ли новый номер с номером в телефоне.
    :rtype numbers: List[str]
    """
    new_number = numbers[0]
    answers = []
    for number in numbers[1:]:
        if number == new_number:
            answers.append("YES")
        else:
            answers.append("NO")
    return answers


def bring_number_to_standard(number: str) -> str:
    """
    Функция которая приводит вид телефонного номера к стандарту.

    :param number: телефонный номер в произвольном виде
    :type number: str

    :return: телефонный номер приведенный к стандарту
    :rtype: str
    """
    number = number.replace('-', '').replace('(', '').replace(')', '')
    if number.startswith('+7'):
        number = number.replace('+7', '8')
    if len(number) <= 7:
        number = '8495' + number
    return number


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    numbers = []
    for _ in range(NUMBERS_COUNT):
        num = input()
        num = bring_number_to_standard(num)
        numbers.append(num)
    print(*check_numbers(numbers), sep='\n')


if __name__ == '__main__':
    main()
