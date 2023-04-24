def solution(price, money, count):
    result = sum([i * price for i in range(1, count + 1)])
    if money - result >= 0:
        return 0
    else:
        return abs(money - result)