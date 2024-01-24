def search_replace(my_list, search, replace):
    if my_list is None:
        return
    n_list = my_list[:]
    for index, c in enumerate(n_list):
        if c == search:
            n_list[index] = replace
    return n_list
