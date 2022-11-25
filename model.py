# Решение задачи из семинара
def parsing(my_str) -> list:
    """
    Парсит строку
    """
    new_list = []
    temp = 0
    for idx,elem in enumerate(my_str):
        if elem in "+-/*":
            new_list.append(int(my_str[temp:idx]))  # добавили 1 temp = 0
            new_list.append(elem) # добавили "+" в new_list
            temp = idx + 1 # индекс "+"
    new_list.append(int(my_str[temp:]))

    return new_list


def run(new_list) -> int:
    """
    Выдает результат выражения из списка
    """
    temp = 0
    tmp_list = new_list.copy()
    length = len(tmp_list)
    idx = 0

    while idx < length:
        elem = tmp_list[idx]
        if elem == '*':
            temp = tmp_list[idx-1] * tmp_list[idx+1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        elif elem == '/':
            temp = tmp_list[idx-1] / tmp_list[idx +1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        else: idx += 1

    length = len(tmp_list)
    idx = 0
    while idx < length:
            elem = tmp_list[idx]
            if elem == '+':
                temp = tmp_list[idx - 1] + tmp_list[idx + 1]
                tmp_list[idx] = temp
                tmp_list.pop(idx + 1)
                tmp_list.pop(idx - 1)
                length -= 2
            elif elem == '-':
                temp = tmp_list[idx - 1] - tmp_list[idx + 1]
                tmp_list[idx] = temp
                tmp_list.pop(idx + 1)
                tmp_list.pop(idx - 1)
                length -= 2
            else:
                idx += 1
    return tmp_list[0]


def read_data(file_name='.TOKEN'):
    '''
    Считывает ТОКИН из файла
    :param file_name: принемает имя и путь к файлу
    :return: строку с данными
    '''
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readline()
        return data


if __name__ == "__main__":

    my_str = "1+2*3-6*5+78"

    # print(parsing(my_str))
    print(run(parsing(my_str)))