X, Y = list(map(int, input().split()))

answer = 0
for i in range(X, Y+1):
    digits = list(map(int, str(i)))
    answer = max(sum(digits), answer)

print(answer)