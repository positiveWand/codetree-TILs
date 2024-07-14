n, m = list(map(int, input().split()))

A = []
B = []
for _ in range(n):
    A.append(input())
for _ in range(n):
    B.append(input())

answer = 0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):

            # 조합이 2가지
            combA = set()
            for a in A:
                combA.add(a[i]+a[j]+a[k])
            
            combB = set()
            for b in B:
                combB.add(b[i]+b[j]+b[k])
            
            if len(combA.intersection(combB)) == 0:
                answer += 1
print(answer)