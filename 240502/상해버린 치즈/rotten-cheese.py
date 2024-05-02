N,M,D,S = tuple(map(int, input().split()))

eat_record = [tuple(map(int, input().split())) for _ in range(D)]
hurt_record = [tuple(map(int, input().split())) for _ in range(S)]

hurt = set()
min_time = {p: float('inf') for p in range(1, N+1)}
# 상한 치즈 후보 찾기
for p, t in hurt_record:
    min_time[p] = min(min_time[p], t)
    hurt.add(p)
# print(hurt)
# print(min_time)
probable = {p: set() for p in range(1, N+1)}
for p, c, t in eat_record:
    if p in hurt and t < min_time[p]:
        probable[p].add(c)


# print(probable)
rotten = set()
for p in hurt:
    if len(rotten) == 0:
        rotten = probable[p]
    rotten &= probable[p]

# print(rotten)


# 상한 치즈 먹은 사람 찾기
answer = set()
for p, c, t in eat_record:
    if c in rotten:
        answer.add(p)

print(len(answer))