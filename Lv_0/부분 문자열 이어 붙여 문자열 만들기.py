def solution(my_strings, parts):
    result = ""
    for i, (a, b) in enumerate(parts):
        result += my_strings[i][a:b+1]
    return result