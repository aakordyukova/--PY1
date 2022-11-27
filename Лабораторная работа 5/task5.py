from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n: int = 8) -> str:
    if not isinstance(n, int):
        raise ValueError("Значение длины пароля задано некорректно")
    return "".join(sample(ascii_uppercase + ascii_lowercase + digits, n))


print(get_random_password())
