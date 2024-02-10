def duplicate_string(n: int, input_string: str) -> str:
    """
    Принимает число n и строку, возвращая ту же строку, продублированную n раз

    :param n: Целое число, количество дубликатов (должно быть неотрицательным)
    :param input_string: Исходная строка для дублирования
    :return: Строка, продублированная n раз

    Примеры:
    duplicate_string(3, 'this is m') -> 'this is mthis is mthis is m'
    duplicate_string(-1, 'example') -> ''  # ValeError при n < 0
    duplicate_string(2, '') -> ''  # Пустая строка при пустой исходной строке
    """
    if n < 0:  # решил добавить проверку на положительность входного числа
        raise ValueError("Количество дубликатов (n) должно быть неотрицательным.")

    return input_string * n


print(duplicate_string(3, 'this is m'))
print(duplicate_string(-1, 'example'))
print(duplicate_string(2, ''))
# почему при множестве итераций результатов ошибка иногда падает до отбработки print(duplicate_string(3, 'this is m'))
