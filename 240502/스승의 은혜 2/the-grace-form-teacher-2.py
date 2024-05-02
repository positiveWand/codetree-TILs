N, B = list(map(int, input().split()))
presents = [int(input()) for _ in range(N)]
presents.sort()

answer = 0

for i in range(N):
    left = presents[:i]+ [presents[i]//2] +presents[i+1:]

    buylist = []
    for l in left:
        if sum(buylist) + l <= B:
            buylist.append(l)
    
    answer = max(answer, len(buylist))

print(answer)