X = int(input())

answer = float('inf')
for x in range(100):
    for y in range(x+1, 100):
        # print(((x+1)*y))
        if X == (x+1)*y:
            answer = min(answer, x+y)
        elif X == (x+1)*y+1:
            answer = min(answer, x+y+1)

print(answer)