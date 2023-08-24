def solution(ineq, eq, n, m):
    answer = 0

    if (ineq, eq) == ('<', '='):
        answer = int(n <= m)
    elif (ineq, eq) == ('>', '='):
        answer = int(n >= m)
    elif (ineq, eq) == ('<', '!'):
        answer = int(n < m)
    elif (ineq, eq) == ('>', '!'):
        answer = int(n > m)
    else:
        return 'wrong input'

    return answer