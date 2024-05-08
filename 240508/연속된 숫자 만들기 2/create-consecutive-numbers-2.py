seq = list(map(int, input().split()))
seq.sort()

if seq[2]-seq[1]==seq[1]-seq[0]==1:
    print(0)
elif seq[2]-seq[1]==2 or seq[1]-seq[0]==2:
    print(1)
else:
    print(2)