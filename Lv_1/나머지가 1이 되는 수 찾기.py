def solution(n):
    result = 1
    while True:
        if n % result == 1:
            return result
            break
        else:
            result += 1