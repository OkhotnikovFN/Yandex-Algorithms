from typing import List


def get_wins_count(board: List[str], symb_type: str) -> int:
    """
    Функция которая вычисляет количество выигрышных позиций для определенного типа.

    :param board: игровая доска
    :type board: List[str]
    :param symb_type: типа знака (крестик или нолик)
    :type symb_type: str

    :return: количество выигрышных позиций
    :rtype: int
    """
    win_lines = [
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    count = 0
    for w in win_lines:
        if board[w[0]] == symb_type and board[w[1]] == symb_type and board[w[2]] == symb_type:
            count += 1
    return count


def get_answer(board: List[str]) -> str:
    """
    Функция которая определяет, возможна для данная ситуация на доске.

    :param board: игровая доска
    :type board: List[str]

    :return: ответ YES или NO
    :rtype: str
    """
    count1 = 0
    count2 = 0
    for i in board:
        if i == '1':
            count1 += 1
        elif i == '2':
            count2 += 1

    win1 = get_wins_count(board, '1')
    win2 = get_wins_count(board, '2')
    if count1 - count2 > 1 or count1 - count2 < 0 or win1 > 2 or win2 > 1 or \
            (win1 and win2) or (win1 and count2 != count1 - 1) or (win2 and count1 != count2):
        ans = 'NO'
    else:
        ans = 'YES'

    return ans


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    board = []
    with open('input.txt', 'r') as f:
        for line in f:
            board.extend(line.strip().split())
    print(get_answer(board))


if __name__ == '__main__':
    main()
