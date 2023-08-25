def solution(num_list):
    str_odd = ''
    str_even = ''
    for i in num_list:
        if i % 2:
            str_odd += str(i)
        else:
            str_even += str(i)
    return int(str_odd) + int(str_even)