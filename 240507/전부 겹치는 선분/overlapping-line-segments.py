n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(1,101):
    fail = False
    for start, end in lines:
        if start <= i <= end:
            fail = False
        else:
            fail = True
            break
    
    if not fail:
        print('Yes')
        break