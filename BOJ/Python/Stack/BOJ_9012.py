# BOJ_9012 괄호

from sys import stdin

input = stdin.readline

def solution():
    t = int(input().rstrip())
    
    for _ in range(t):
        vps = list(map(str, input().rstrip()))
        
        stack = []
        flag = True

        for string in vps:
            if string == '(':
                stack.append(string)
            else:
                if len(stack) == 0:
                    flag = False
                    break
                else:
                    stack.pop()
        
        if flag and len(stack) == 0:
            print("YES")
        else:
            print("NO")

solution()