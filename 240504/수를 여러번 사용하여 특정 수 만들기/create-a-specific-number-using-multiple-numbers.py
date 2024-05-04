A, B, C = tuple(map(int, input().split()))

answer = 0

i = 0
while i*A < C:
    j = 0
    while i*A+j*B < C:
        answer = max(i*A+j*B, answer)

        j += 1
    
    i += 1

print(answer)