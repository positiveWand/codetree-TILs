n, m = list(map(int, input().split()))

num = list(map(int, input().split()))
query = list(map(int, input().split()))

count = {}
for n in num:
    if n not in count:
        count[n] = 0
    count[n] += 1

answer = []
for q in query:
    if q in count:
        answer.append(str(count[q]))
    else:
        answer.append('0')

print(' '.join(answer))