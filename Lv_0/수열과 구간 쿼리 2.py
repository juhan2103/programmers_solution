def solution(arr, queries):
    result = []
    for query in queries:
        lst = []
        for i in range(query[0], query[1] + 1):
            if arr[i] > query[2]:
                lst.append(arr[i])
        try:
            result.append(min(lst))
        except:
            result.append(-1)
    return result