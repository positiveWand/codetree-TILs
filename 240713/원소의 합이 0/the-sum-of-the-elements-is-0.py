n = int(input())
arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))

count1 = {}
count2 = {}
for i in range(n):
    for j in range(n):
        v1 = arr[0][i] + arr[1][j]
        if v1 not in count1:
            count1[v1] = 0
        count1[v1] += 1

        v2 = arr[2][i] + arr[3][j]
        if v2 not in count2:
            count2[v2] = 0
        count2[v2] += 1
# print(count1)
# print(count2)
answer = 0
for n in count1:
    if -n in count2 and count2[-n] >= 1:
        answer += count1[n] * count2[-n]
        count2[-n] -= 1

print(answer)