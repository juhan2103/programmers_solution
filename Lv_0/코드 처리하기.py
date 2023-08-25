def solution(code):
    ret = ''
    mode = 0
    for idx, i in enumerate(code):
        if mode == 0:
            if i != '1':
                if idx % 2 == 0:
                    ret += i
            elif i == '1':
                mode = 1
        elif mode == 1:
            if i != '1':
                if idx % 2:
                    ret += i
            elif i == '1':
                mode = 0
    if ret == '':
        return 'EMPTY'
    else:
        return ret