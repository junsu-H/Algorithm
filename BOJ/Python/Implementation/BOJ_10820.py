# BOJ_10820 문자열 분석

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    while True:
        lower = 0
        upper = 0
        number = 0
        space = 0
        string = sys.stdin.readline().rstrip('\n')

        if not string:
            break

        for i in range(len(string)):
            if string[i].islower():
                lower += 1
            elif string[i].isupper():
                upper += 1
            elif string[i].isnumeric():
                number += 1
            else:
                space += 1 
        
        print(lower, upper, number, space)
        
solution()