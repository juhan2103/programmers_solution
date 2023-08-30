def solution(emergency):
    result = []
    idx_list = sorted(emergency, reverse = True)
    for i in emergency:
        result.append(idx_list.index(i) + 1)
    return result