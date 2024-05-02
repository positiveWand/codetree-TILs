N, K = list(map(int, input().split()))
bombs = [int(input()) for _ in range(N)]

answer = -1
for i in range(N):
    ignite = False
    for j in range(max(0, i-K), min(N, i+K)):
        if i != j and bombs[i] == bombs[j]:
            ignite = True
            break

    if ignite:
        answer = max(answer, bombs[i])

print(answer)