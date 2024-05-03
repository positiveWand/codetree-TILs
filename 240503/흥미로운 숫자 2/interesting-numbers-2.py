X, Y = tuple(map(int, input().split()))
answer = 0
for test_num in range(X, Y+1):
    digits = list(map(int, list(str(test_num))))
    count = dict()
    for d in digits:
        if d not in count:
            count[d] = 0
        count[d] += 1
    
    if len(count) == 2:
        for v in count.values():
            if v == 1:
                answer += 1
                break

print(answer)