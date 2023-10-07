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




def kth_largest_in_list(input_list, kth_largest):
    if kth_largest <= 0 or kth_largest > len(input_list):
        return None
    sorted_list = sorted(input_list, reverse=True)
    return sorted_list[kth_largest - 1]




def cumavg_list(input_list):
    if not input_list:
        return []

    cumulative_sum = 0
    cumulative_avg_list = []

    for i, value in enumerate(input_list):
        cumulative_sum += value
        avg = cumulative_sum / (i + 1)
        cumulative_avg_list.append(avg)

    return cumulative_avg_list


def element_wise_multiplication(input_list1, input_list2):
    if len(input_list1) != len(input_list2):
        return None

    result_list = []

    for i in range(len(input_list1)):
        product = input_list1[i] * input_list2[i]
        result_list.append(product)

    return result_list


def merge_lists(*lists):
    merged_list = []

    for lst in lists:
        merged_list.extend(lst)

    return merged_list




def squared_odds(input_list):
    odd_squares = []
    for number in input_list:
        if number % 2 != 0:
            odd_squares.append(number ** 2)
    return odd_squares




def reverse_sort_by_key(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[0], reverse=True))
    return sorted_dict




def sort_list_by_divisibility(input_list):
    by_two = []
    by_five = []
    by_two_and_five = []
    by_none = []

    for num in input_list:
        if num % 2 == 0 and num % 5 == 0:
            by_two_and_five.append(num)
        elif num % 2 == 0:
            by_two.append(num)
        elif num % 5 == 0:
            by_five.append(num)
        else:
            by_none.append(num)

    result_dict = {
        'by_two': by_two,
        'by_five': by_five,
        'by_two_and_five': by_two_and_five,
        'by_none': by_none
    }

    return result_dict
