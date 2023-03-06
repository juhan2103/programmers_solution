def solution(n):
    result = ''
    for i in sorted(str(n), reverse = True):
        result += i
    return int(result)