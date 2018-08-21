from enum import Enum

single_digit = ['bir', 'iki', 'üç', 'dörd', 'beş', 'altı', 'yeddi', 'səkkiz', 'doqquz']
double_digit = ['on', 'iyirmi', 'otuz', 'qırx', 'əlli', 'altmış', 'yetmiş', 'səksən', 'doğsan']


def length(a):
    length = 0
    while a > 0:
        a = a // 10
        length += 1

    return length


class NumberLength(Enum):
    SINGLE_DIGIT = 1 << 0
    DOUBLE_DIGIT = 1 << 1
    THREE_DIGIT = SINGLE_DIGIT | DOUBLE_DIGIT
    FOUR_DIGIT = 1 << 2


def get_word_by_position(value, position):
    if position == NumberLength.SINGLE_DIGIT:
        return single_digit[value - 1]
    elif position == NumberLength.DOUBLE_DIGIT:
        return double_digit[value - 1]
    elif position == NumberLength.THREE_DIGIT:
        return single_digit[value - 1] + ' yüz'
    elif position == NumberLength.FOUR_DIGIT:
        return single_digit[value - 1] + ' min'


def convert_num_to_words(value):
    result = None

    _len = length(value)

    if _len == NumberLength.SINGLE_DIGIT:
        return get_word_by_position(value, NumberLength.SINGLE_DIGIT)

    elif _len == NumberLength.DOUBLE_DIGIT:
        _first_digit = value // 10
        _last_digit = value % 10

        _first_word = get_word_by_position(_first_digit, NumberLength.DOUBLE_DIGIT)
        _last_word = get_word_by_position(_last_digit, NumberLength.SINGLE_DIGIT)

        return _first_word + ' ' + _last_word

    elif _len == NumberLength.THREE_DIGIT:
        _first_digit = value // 100
        _second_digit = (value % 100) // 10
        _last_digit = (value % 100) % 10

        _first_word = get_word_by_position(_first_digit, NumberLength.THREE_DIGIT)
        _second_word = get_word_by_position(_second_digit, NumberLength.DOUBLE_DIGIT)
        _last_word = get_word_by_position(_last_digit, NumberLength.SINGLE_DIGIT)

        if _first_digit == 1:
            _first_word = 'yüz'

        return _first_word + ' ' + _second_word + ' ' + _last_word

    elif _len == NumberLength.FOUR_DIGIT:
        _first_digit = value % 10
        _second_digit = (value // 10) % 10
        _third_digit = (value // 100) % 10
        _last_digit = value // 1000

        _first_word = get_word_by_position(_first_digit, NumberLength.SINGLE_DIGIT)
        _second_word = get_word_by_position(_second_digit, NumberLength.DOUBLE_DIGIT)
        _third_word = get_word_by_position(_third_digit, NumberLength.THREE_DIGIT)
        _last_word = get_word_by_position(_last_digit, NumberLength.FOUR_DIGIT)

        if _last_digit == 1:
            _last_word = 'min'

        if _third_word == 1:
            _third_word = 'yüz'

        return _last_word + ' ' + _third_word + ' ' + _second_word + ' ' + _first_word

    return ''
