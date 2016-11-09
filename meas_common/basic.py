def swap_tmp(input_a, input_b):
    tmp = input_a
    input_a = input_b
    input_b = tmp

    return input_a, input_b


def swap_no_tmp(input_a, input_b):
    input_a += input_b
    input_b = input_a - input_b
    input_a -= input_b

    return input_a, input_b
