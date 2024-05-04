n, m = tuple(map(int, input().split()))
seq = list(map(int, input().split()))

answer = 0
for i in range(n):
    subsum = 0
    current = i
    for j in range(m):
        current = seq[current]-1
        subsum += seq[current]
    
    answer = max(answer, subsum)

print(answer)