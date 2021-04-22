# BOJ_10808 알파벳 개수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = sys.stdin.readline().rstrip()
    alpha = {}

    for i in range(97, 123):
        alpha[chr(i)] = 0
    
    for key in string:
        alpha[key] += 1
    
    for value in alpha.values():
        print(value, end = ' ')

solution()