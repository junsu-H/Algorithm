# BOJ_11536 줄 세우기

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    name = [input().rstrip() for _ in range(n)]
    name_asc = sorted(name)
    name_desc = sorted(name, reverse = True)
    asc = False
    desc = False
    
    for i in range(n):
        if name[i] != name_asc[i]:
            asc = False
            break
        else:
            asc = True
    
    for i in range(n):
        if name[i] != name_desc[i]:
            desc = False
            break
        else:
            desc = True
    
    if asc:
        print("INCREASING")
    elif desc:
        print("DECREASING")
    else:
        print("NEITHER")        

solution()