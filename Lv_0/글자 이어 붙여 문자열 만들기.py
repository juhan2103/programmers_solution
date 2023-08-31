def solution(my_string, index_list):
    string_list = [i for i in my_string]
    result = ''
    for i in index_list:
        result += string_list[i]
    return result