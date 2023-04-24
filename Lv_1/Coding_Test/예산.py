def solution(d, budget):
    answer = 0
    count = 0
    d.sort()
    for i in d:
        answer += i
        if answer > budget:
            break
        else:
            count += 1
    return count