def solution(a, b, c):
    result = 0
    result = a + b + c
    if a == b or b == c or a == c:
        result = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    if a == b == c:
        result = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    return result