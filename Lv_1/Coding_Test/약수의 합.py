def solution(n):
    n_list = []
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(n // i)
    return sum(n_list)