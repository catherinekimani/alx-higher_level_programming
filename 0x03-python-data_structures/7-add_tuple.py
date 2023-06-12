#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_elem = tuple_a + (0, 0)
    second_elem = tuple_b + (0, 0)

    first_res = 0
    second_res = 0

    first_res += first_elem[0] + second_elem[0]
    second_res += first_elem[1] + second_elem[1]
    return (first_res, second_res)
