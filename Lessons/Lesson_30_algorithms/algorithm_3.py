def remove_one_char(frase: str) -> str:
    """
    принимает строку и возвращает ту же без первого и последнего символа

    Примеры:
    (remove_one_char('this is my') -> ‘his is m’
    """
    return frase[1:-1]


print(remove_one_char('this is my'))
# я не учитывал, что строка может быть пустой или состоять из двух символов. нужно было?
# по тз функция верна в принципе
