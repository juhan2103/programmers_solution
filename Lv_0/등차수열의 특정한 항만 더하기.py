def solution(a, d, included):
    answer = 0
    if included[0] == True:
        answer += a
    for i in range(1, len(included)):
        if included[i] == True:
            a += d
            answer += a
        else:
            a += d
    return answer