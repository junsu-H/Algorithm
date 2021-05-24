# BOJ_10987 모음의 개수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = sys.stdin.readline().rstrip()
    vowel = ["a", "e", "i", "o", "u"]
    answer = 0

    for s in string:
        if s in vowel:
            answer += 1
    
    print(answer)
    
solution()