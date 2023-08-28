def solution(angle):
    angles = { 180: 4, 91: 3, 90: 2, 0: 1}
    for base, answer in angles.items():
        if angle >= base:
            return answer