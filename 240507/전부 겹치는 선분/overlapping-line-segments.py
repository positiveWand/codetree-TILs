n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
printed = False
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
        printed = True
        break

if not printed:
    print('No')