def solution(my_string):
    answer = [0 for i in range(52)]
    k = 0
    for my_string in my_string:
        if my_string.isupper(): k = 65
        else: k = 71
        answer[ord(my_string)-k] += 1
    return answer