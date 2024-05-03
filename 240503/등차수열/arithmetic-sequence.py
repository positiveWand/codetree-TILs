n = int(input())
sequence = list(map(int, input().split()))

answer = 0
for k in range(100):
    hit = 0
    for i in range(n):
        for j in range(i+1, n):
            if k == (sequence[i] + sequence[j]) / 2:
                hit += 1
    
    answer = max(hit, answer)

print(answer)