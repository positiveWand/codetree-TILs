n, k = list(map(int, input().split()))

seats = list(range(n))
seated = {
    i: set([i])
    for i in range(n)
}

swaps = []
for _ in range(k):
    ai, bi = list(map(int, input().split()))
    swaps.append((ai-1, bi-1))

for _ in range(3):
    for swap in swaps:
        a, b = swap

        seated[seats[a]].add(b)
        seated[seats[b]].add(a)

        # 자리 바꾸기
        seats[a], seats[b] = seats[b], seats[a]

for i in range(n):
    print(len(seated[i]))