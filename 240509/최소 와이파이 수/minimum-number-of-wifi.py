n, m = tuple(map(int, input().split()))
status = list(map(int, input().split()))
available = [False if status[i]==1 else True for i in range(n)]

wifi = 0
while not all(available):
    max_count = -1
    max_pos = None

    for i in range(n):
        count = 0
        for j in range(max(0, i-m), min(n, i+m+1)):
            if status[j] == 1 and not available[j]:
                count += 1
        
        if count > max_count:
            max_count = count
            max_pos = i

    for i in range(max(0, max_pos-m), min(n, max_pos+m+1)):
        available[i] = True
    # print(max_pos)
    wifi += 1

print(wifi)