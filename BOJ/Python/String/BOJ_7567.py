# BOJ_7567 그릇

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = sys.stdin.readline().rstrip()
    answer = 10

    for i in range(len(string)):
        if string[i] == string[i-1]:
            answer += 5
        else:
            answer += 10
            
    print(answer)
solution()
