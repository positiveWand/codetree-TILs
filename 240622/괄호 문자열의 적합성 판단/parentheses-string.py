string = input()

stack = []

def valid(string):
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0 or stack[-1] != '(':
                return False
                break
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

if valid(string):
    print('Yes')
else:
    print('No')