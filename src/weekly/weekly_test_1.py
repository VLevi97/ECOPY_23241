def evens_from_list(input_list):
    even_numbers = []
    for number in input_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def every_element_is_odd(input_list):
    for bool in input_list:
        if bool % 2 == 0:
            return False
    return True


def squared_odds(input_list):
    odd_squares = []
    for number in input_list:
        if number % 2 != 0:
            odd_squares.append(number ** 2)
    return odd_squares