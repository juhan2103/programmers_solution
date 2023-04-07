def gcd(a, b):
    while b != 0:
        remain = b
        b = a % b
        a = remain
    return a
def solution(n, m):
    lcm = (n // gcd(n, m)) * (m // gcd(n, m)) * gcd(n, m)
    answer = [gcd(n, m), lcm]
    return answer