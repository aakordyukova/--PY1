# TODO написать функцию для получения списка уникальных целых чисел
from random import randint


def get_unique_list_numbers() -> list[int]:
    min_num = -10
    max_num = 10
    length = 15
    list_ = [randint(min_num, max_num) for _ in range(length)]
    while len(set(list_)) != length:
        list_ = list(set(list_))
        list_.append(randint(min_num, max_num))
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
