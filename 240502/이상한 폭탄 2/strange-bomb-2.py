N, K = list(map(int, input().split()))
bombs = [int(input()) for _ in range(N)]

answer = -1

# 각 폭탄을 기준으로 반경 K를 검사하여 같은 종류의 폭탄 탐색
for i in range(N):
    ignite = False
    for j in range(max(0, i-K), min(N, i+K)):
        # 주의 - 자기 자신은 검사대상에서 제외
        if i != j and bombs[i] == bombs[j]:
            ignite = True
            break

    if ignite:
        answer = max(answer, bombs[i])

print(answer)