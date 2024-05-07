n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(n-1, 0, -1):
    need = B[i] - A[i]

    current = i-1
    while 0<need:
        available = min(need, A[current])
        A[current] -= available
        need -= available
        A[i] += available
        answer += available * (i-current)
        current -= 1

print(answer)