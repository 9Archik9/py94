def sum_all_positive_numbers(numbers: list) -> int:
    """
    принимает список целых чисел и возвращает суммму положительных

    Примеры:
    (sum_all_positive_numbers([1, 2, -4, 7]) -> 10
    sum_all_positive_numbers([-1, -5]) -> 0
    """
    return sum(num for num in numbers if num > 0)


print(sum_all_positive_numbers([1, 2, -4, 7]))
print(sum_all_positive_numbers([-1, -5]))
