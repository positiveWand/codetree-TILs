hints = list(map(int, input().split()))
hints.sort()

for a in range(1,41):
    for b in range(1,41):
        for c in range(1,41):
            for d in range(1,41):
                test = [
                    a,
                    b,
                    c,
                    d,
                    a+b,
                    b+c,
                    c+d,
                    d+a,
                    a+c, b+d,
                    a+b+c,
                    a+b+d,
                    a+c+d,
                    b+c+d,
                    a+b+c+d
                ]

                test.sort()
                if test == hints:
                    print(a,b,c,d)
                    exit()