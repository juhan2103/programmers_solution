def solution(arr,divisor):
    result = []
    for i in sorted(arr):
        if i % divisor == 0:
            result.append(i)
    if len(result) == 0:
        return [-1]
    else:
        return result