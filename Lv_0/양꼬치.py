def solution(n, k):
    service = n // 10 * 2000
    answer = n * 12000 + k * 2000 - service
    return answer