# 두 수의 합

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    x = int(sys.stdin.readline().rstrip())
    
    array.sort()
    left, right = 0, n-1
    answer = 0

    while left < right:
        temp = array[left] + array[right]
        if temp == x:
            answer += 1
        
        if temp < x:
            left += 1
            continue

        right -= 1
    
    print(answer)        
    
solution()
