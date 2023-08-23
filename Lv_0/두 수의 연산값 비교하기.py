def solution(a, b):
    result = int(str(a) + str(b))
    return max(result, 2 * a * b)