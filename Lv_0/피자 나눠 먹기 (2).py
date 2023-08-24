n = 10
cnt = 1
pizza = 6
while True:
    if pizza % n == 0:
        print(cnt)
        break
    else:
        cnt += 1
        pizza * cnt
    