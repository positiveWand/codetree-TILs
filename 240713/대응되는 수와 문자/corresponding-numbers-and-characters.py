n, m = tuple(map(int, input().split()))

ntos = {}
ston = {}
for i in range(1,n+1):
    string = input()
    ntos[i] = string
    ston[string] = i

for _ in range(m):
    query = input()
    if query.isdigit():
        print(ntos[int(query)])
    else:
        print(ston[query])