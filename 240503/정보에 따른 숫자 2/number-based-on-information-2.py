T, a, b = tuple(map(int, input().split()))
points = [input().split() for _ in range(T)]
points = list(map(lambda x: (x[0], int(x[1])), points))

answer = 0
for i in range(a, b+1):
    closest_s = min(list(filter(lambda x: x[0]=='S', points)), key=lambda x: abs(x[1]-i))
    closest_n = min(list(filter(lambda x: x[0]=='N', points)), key=lambda x: abs(x[1]-i))
    # print(closest_n, closest_s, i)

    if abs(i-closest_s[1]) <= abs(i-closest_n[1]):
        answer += 1

print(answer)