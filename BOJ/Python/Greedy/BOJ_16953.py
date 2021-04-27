# BOJ_16953 A -> B

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    count = 1

    while True:
        if a == b:
            break
        elif (b % 2 != 0 and b % 10 != 1) or (b < a):
            count = -1   
            break
        else:
            if b % 2 == 0:
                b //= 2
                count += 1
            elif b % 2 == 1:
                b //= 10
                count += 1

    print(count)

solution()