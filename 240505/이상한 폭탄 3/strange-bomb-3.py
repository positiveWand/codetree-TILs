N, K = tuple(map(int, input().split()))

bombs = [int(input()) for _ in range(N)]
exploded = dict()

most = 0
answer = 0
for num in set(bombs):
    count = 0
    for i, bomb in enumerate(bombs):
        if bomb == num and num in set(bombs[max(0,i-K):i]+bombs[i+1:i+K+1]):
            count += 1

    if answer < count:
        answer = count
        most = num

print(most)