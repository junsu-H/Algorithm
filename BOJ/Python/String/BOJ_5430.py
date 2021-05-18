# BOJ_5430 AC

import sys
sys.setrecursionlimit(10 ** 9)
from collections import deque

def solution():
    t = int(sys.stdin.readline().rstrip())
    
    for i in range(t):
        rev_count = 0
        err_flag = False

        p = sys.stdin.readline().rstrip()

        n = int(sys.stdin.readline().rstrip())
        array = sys.stdin.readline().rstrip()[1:-1].split(",")
        array = deque(array)

        for string in p:
            if string == 'R':
                rev_count += 1
            elif string == 'D':
                if n == 0:
                    err_flag = True
                    break
                
                if rev_count % 2 == 0:
                    array.popleft()
                elif rev_count % 2 == 1:
                    array.pop()
                n -= 1
                    
        if rev_count % 2 == 1:
            array.reverse()
        
        if err_flag:
            print("error")
        else:
            print('[' + ','.join(array) + ']')

solution()