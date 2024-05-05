n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
# print(ranges)

answer = None
for x in range(1, 10001):
    current = x * 2

    good = True
    for start, end in ranges:
        if not (start <= current <= end):
            good = False
            break
        current = current * 2
    
    if good:
        answer = x
        break

print(answer)