K, N = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(K)]

answer = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        fail = False
        for dev in orders:
            if dev.index(i+1) > dev.index(j+1):
                fail = True
                break
        
        if not fail:
            # print(i, j)
            answer += 1

print(answer)