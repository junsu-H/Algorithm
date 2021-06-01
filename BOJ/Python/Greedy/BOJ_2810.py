# BOJ_2810 컵홀더

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    string = sys.stdin.readline().rstrip()
    
    if string.count("LL"):
        print(len(string.replace("LL", "S")) + 1)
    else:
        print(n)

solution()