# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

dict_list = [{"bin": bin(num), "dec": num, "oct": oct(num), "hex": hex(num)} for num in range(16)]
pprint(dict_list)

# TODO записать словарь десятичных и шестадцатиричных чисел
dict_hex = {num: hex(num) for num in range(16)}
print(dict_hex)