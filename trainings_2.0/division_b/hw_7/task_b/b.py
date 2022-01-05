from typing import List, Tuple


START = 1
END = -1


def get_device_count(incoming_devices: List[Tuple[int, int]]) -> int:
    """
    Функция которая вычисляет минимальное количество требуемых аппаратов.

    :param incoming_devices: список событий, с началом и концом обслуживания посылок
    :type incoming_devices: List[Tuple[int, int]]

    :return: минимальное количество требуемых аппаратов
    :rtype: int
    """
    online = 0
    max_online = 0

    for event in incoming_devices:
        if event[1] == START:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)

    return max_online


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    N = int(input())

    incoming_devices = []
    for _ in range(N):
        T, L = map(int, input().split())
        incoming_devices.append((T, START))
        incoming_devices.append((T + L, END))
    incoming_devices.sort()

    print(get_device_count(incoming_devices))


if __name__ == '__main__':
    main()
