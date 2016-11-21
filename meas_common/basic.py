"""
# Name:           meas_common/basic.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   N.A
# Last Modified:  Nov 21 2016
# Modified by:    Phuc Le-Sanh
"""


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
