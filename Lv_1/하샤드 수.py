def solution(arr):
    result = 0
    for i in str(arr):
        result += int(i)
    if arr % result == 0:
        return True
    else:
        return False