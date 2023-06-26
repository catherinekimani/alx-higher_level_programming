#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(list_length):
        try:
            div_result = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("divison by 0")
            div_result = 0
        except TypeError:
            print("wrong type")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            result.append(div_result)
    return result
