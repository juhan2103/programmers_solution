def solution(n):
    answer = []
    while n != 1:
        if n % 2:
            answer.append(n)
            n = 3 * n + 1
        else:
            answer.append(n)
            n //= 2
    answer.append(1)
    return answer