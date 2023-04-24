import itertools
def solution(number):
    answer = 0
    threes = itertools.combinations(number, 3)
    for three in threes:
        if sum(three) == 0:
            answer += 1
    return answer