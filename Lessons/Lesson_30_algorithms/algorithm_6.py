import re  # встроенный модуль питона для работы c текстом(регулярные выражения)


def ordered_string(unordered_str: str) -> str:
    """
    Функция принимает неупорядоченную строку состоящую из слов разделенных пробелами,
    каждое слово содержит помимо слова число (wor4d) - свою будущую позицию.
    Функция должна возвращать упорядоченную строку, где все слова будут соответствовать своим позициям

    Note: та же функция, но учитывающее, что в слове может быть цифра > 9

    :param unordered_str: ‘2is Thi1s numb4er m3y tu10 n5ne s6x 8ght 9ine 11ven 7even
    :return: Thi1s 2is m3y numb4er n5ne s6x 7even 8ght 9ine tu10 11ven

    Примеры:
    ordered_string('2is Thi1s numb4er m3y tu10 n5ne s6x 8ght 9ine 11ven 7even')) ->
    Thi1s 2is m3y numb4er n5ne s6x 7even 8ght 9ine tu10 11ven
    """
    split_string = unordered_str.split(' ')
    answer_list = []

    for word in split_string:
        regex_match = re.search(r'(\d+)', word)
        if regex_match:
            position = int(regex_match.group())
            answer_list.append((position, word))

    answer_list.sort(key=lambda x: x[0])

    ordered_words = [word[1] for word in answer_list]
    answer_string = ' '.join(ordered_words)
    return answer_string


print(ordered_string('2is Thi1s numb4er m3y tu10 n5ne s6x 8ght 9ine 11ven 7even'))


def order_words(unordered_str: str) -> str:
    """
    та же функция но быстрее за счет встроенного метода sort и отсутсвия цикла for
    """
    words = unordered_str.split()

    ordered_words = sorted(words, key=lambda x: int(''.join(filter(str.isdigit, x))))
    ordered_str = ' '.join(ordered_words)

    return ordered_str


print(order_words('2is Thi1s numb4er m3y tu10 n5ne s6x 8ght 9ine 11ven 7even'))
