def solution(x, n):
    n_list = []
    value = x
    for i in range(n):
        n_list.append(x)
        x += value
    return n_list