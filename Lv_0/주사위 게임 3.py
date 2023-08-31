def solution(a, b, c, d):
    result = 0
    origin = [a, b, c, d]
    arr = list(set(origin))
    
    if len(arr) == 4:
        result = min(arr)
    elif len(arr) == 3:
        p = max(origin, key=origin.count)
        tmp = [num for num in arr if num != p]
        result = tmp[0] * tmp[1]
    elif len(arr) == 2:
        if max([origin.count(num) for num in arr]) > 2:
            p = max(origin, key=origin.count)
            q = min(origin, key=origin.count)
            result = pow(((10*p)+q),2)
        else:
            result = (arr[0] + arr[1]) * abs(arr[0] - arr[1])
    elif len(arr) == 1:
        result = 1111 * arr[0]
    return result