def solution(numbers, direction):
    tmp = 0
    if direction == "right":
        tmp = numbers.pop()
        numbers.insert(0,tmp)
    elif direction == 'left':
        tmp = numbers.pop(0)
        numbers.insert(len(numbers), tmp)
    return numbers