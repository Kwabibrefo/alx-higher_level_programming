#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divs = []
    for index in range(list_length):
        res = 0
        try:
            res = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            divs.append(res)
    return divs
