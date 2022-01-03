def get_theme_name(messages_count) -> str:
    """
    Функция которая определяет наиболее встречающуюся тему.

    :param messages_count: количество сообщений
    :type messages_count: int

    :return: название наиболее встречающейся темы
    :rtype: str
    """

    themes_list = []
    themes_dict_messages_count = {}
    themes_dict_index = {}

    for index in range(1, messages_count + 1):
        new_message = input()
        if new_message.isdigit():
            int_message = int(new_message)
            if int_message == 0:
                theme = input()
                message = input()
                themes_list.append(theme)
                themes_dict_messages_count[theme] = 1
                themes_dict_index[theme] = [index]
            else:
                message = input()
                for theme_name, themes_indexes in themes_dict_index.items():
                    if int_message in themes_indexes:
                        themes_dict_messages_count[theme_name] += 1
                        themes_dict_index[theme_name].append(index)
                        break

    max_voices = max(themes_dict_messages_count.values())

    for theme_name in themes_list:
        if themes_dict_messages_count[theme_name] == max_voices:
            return theme_name


def main():
    """Основная функция для чтения входных данных и вывода результата."""
    n = int(input())
    print(get_theme_name(n))


if __name__ == '__main__':
    main()
