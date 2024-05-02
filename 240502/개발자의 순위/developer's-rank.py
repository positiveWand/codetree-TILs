K, N = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(K)]

answer = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        fail = False
        for order in orders:
            if order[i] > order[j]:
                fail = True
                break
        
        if not fail:
            answer += 1

print(answer)