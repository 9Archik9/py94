def digital_root(num: int) -> int:
    """
    принимает число больше 9 и вычисляет его цифровой корень
    note: цифровой корень вычисляется только для абсолютных значений числа (модуль числа)

    :param num: Целое число > 9
    :return: Цифровой корень числа
    :raises ValueError: Если num не является целым числом или < 10

    Примеры:
    print(digital_root(16)) -> 7
    print(digital_root(942) -> 9 + 4 + 2 = 15 -> 1 + 5 -> 6
    print(digital_root(132189)) -> 1 + 3 + 2 + 1 + 8 + 9 = 24 -> 2 + 4 -> 6
    print(digital_root(-99)) -> 9
    print(digital_root(8)) -> ValueError
    print(digital_root(99.9)) -> ValueError

    """

    num = abs(num)  # так как цифровой корень считается только для положительных чисел

    if num <= 9 or not isinstance(num, int):
        raise ValueError("число должно быть целым и больше 9")
    while num > 9:
        num = sum(map(int, str(num)))  # соблюдается ли тут читаемость кода :) ?

    return num


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(-99))
print(digital_root(-8))
print(digital_root(99.9))
