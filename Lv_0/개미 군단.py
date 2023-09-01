def solution(hp):
    result = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        result += d
    return result