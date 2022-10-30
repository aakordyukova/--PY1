def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    char_count_dict = {}
    DEFAULT_COUNT = 0
    for char in str_:
        if char.isalpha():
            char_count_dict[char] = char_count_dict.get(char, DEFAULT_COUNT) + 1

    return char_count_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_percent_char(char_count_dict):
    percent_char_dict = {}
    total_chars = sum(char_count_dict.values())
    for unique_char, count_char in char_count_dict.items():
        percent_char_dict[unique_char] = round(((count_char / total_chars) * 100), 2)

    return percent_char_dict
