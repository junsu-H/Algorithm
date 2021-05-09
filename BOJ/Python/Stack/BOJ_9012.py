import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    t = int(sys.stdin.readline().rstrip())
    
    for _ in range(t):
        vps = list(map(str, sys.stdin.readline().rstrip()))
        
        stack = []
        flag = True

        for string in vps:
            if string == '(':
                stack.append(string)
            else:
                if len(stack) == 0 or stack[len(stack) - 1] == ')':
                    flag = False
                    break
                else:
                    stack.pop()
        
        if flag and len(stack) == 0:
            print("YES")
        else:
            print("NO")

solution()