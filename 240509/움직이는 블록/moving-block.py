N = int(input())
status = [int(input()) for _ in range(N)]

avg = sum(status) // len(status)

answer = 0 
for s in status:
    if s > avg:
        answer += s-avg
print(answer)