def solution(my_string, is_suffix):
    lst = []
    for i in range(len(my_string)):
        lst.append(my_string[i:])
    if is_suffix in lst:
        return 1
    else:
        return 0