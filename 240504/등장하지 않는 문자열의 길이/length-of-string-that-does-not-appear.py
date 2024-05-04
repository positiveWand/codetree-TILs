N = int(input())
string = input()

for length in range(1, N):
    substrings = set()
    success = True
    for start in range(N-length+1):
        substring = string[start:start+length]
        if substring in substrings:
            success = False
            break
        else:
            substrings.add(substring)
    
    if success:
        print(length)
        break