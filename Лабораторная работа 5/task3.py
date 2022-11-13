from random import randint


def get_unique_list_numbers(min_num: int = -10, max_num: int = 10, length: int = 15) -> list[int]:
    if not isinstance(min_num, int):
        raise ValueError("Минимальное число задано некорректно")
    if not isinstance(max_num, int):
        raise ValueError("Максимальное число задано некорректно")
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Значение длины листа задано некорректно")
    if (max_num - min_num + 1) < length:
        raise ValueError("С такими параметрами невозможно создать список из уникальных чисел")
    list_ = [randint(min_num, max_num) for _ in range(length)]
    while len(set(list_)) != length:
        list_ = list(set(list_))
        list_.append(randint(min_num, max_num))
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))