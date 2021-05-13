# BOJ_1259 팰린드롬수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    while True:
        number = sys.stdin.readline().rstrip('\n')
        
        if not int(number):
            break
        
        if number == number[::-1]:
            print('yes')
        else:
            print('no')

solution()