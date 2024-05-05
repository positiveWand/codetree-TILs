N = int(input())
neighbor_sums = list(map(int, input().split()))

for first in range(1, N+1):
    original = [first]

    fail = False
    current = first
    for n in neighbor_sums:
        new = n-current
        if new in original or not (0<=new<=n):
            fail = True
            break
        else:
            original.append(new)
            current = new
    
    if fail:
        continue
    else:
        print(' '.join(list(map(str, original))))
        break