N = int(input())
iceburgs = [int(input()) for _ in range(N)]

answer = 0
for level in range(1001):
    above = [i > level for i in iceburgs]

    count = 0
    for i, a in enumerate(above):
        if i == len(above)-1 and a:
            count += 1
        elif a and not above[i+1]:
            count += 1

    
    answer = max(answer, count)

print(answer)