#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    newlist[idx] = element
    if (idx >= 0) and (idx < len(my_list)):
        return (newlist)
    else:
        return (my_list)
