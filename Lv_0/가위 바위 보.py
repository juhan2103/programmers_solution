def solution(rsp):
    lst = {'2': '0', '0': '5', '5': '2'}
    result = ''
    for i in rsp:
        result += lst[i]
    return result