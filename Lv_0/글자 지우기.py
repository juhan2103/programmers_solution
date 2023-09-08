def solution(my_string, indices):
    result = ''
    my_list = list(my_string)
    for i in indices:
        my_list[i] = ""
    my_list.remove("")
    return "".join(my_list)