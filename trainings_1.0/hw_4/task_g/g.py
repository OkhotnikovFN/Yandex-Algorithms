from typing import List, Union


def get_balance(file_name: str) -> List[Union[int, str]]:
    """
    Функция которая вычисляет баланс для каждого клиента банка.
        Параметры:
            :param file_name: имя считываемого файла
            :type file_name: str
        Возвращаемое значение:
            :return: список балансов клиентов
            :rtype: List[]
    """
    result = []
    clients = {}

    with open(file_name) as file:
        for line in file:
            command = line.split()
            if command[0] == 'DEPOSIT':
                name = command[1]
                if name in clients:
                    clients[name] += int(command[2])
                else:
                    clients[name] = int(command[2])
            elif command[0] == 'WITHDRAW':
                name = command[1]
                if name in clients:
                    clients[name] -= int(command[2])
                else:
                    clients[name] = -int(command[2])
            elif command[0] == 'BALANCE':
                name = command[1]
                if name in clients:
                    result.append(clients[name])
                else:
                    result.append('ERROR')
            elif command[0] == 'TRANSFER':
                name1 = command[1]
                name2 = command[2]
                if name1 in clients:
                    clients[name1] -= int(command[3])
                else:
                    clients[name1] = -int(command[3])
                if name2 in clients:
                    clients[name2] += int(command[3])
                else:
                    clients[name2] = int(command[3])
            elif command[0] == 'INCOME':
                percent = int(command[1])
                for name in clients:
                    if clients[name] > 0:
                        clients[name] = int(clients[name] * (1 + percent / 100))
    return result


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    file_name = 'input.txt'
    result = get_balance(file_name)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
