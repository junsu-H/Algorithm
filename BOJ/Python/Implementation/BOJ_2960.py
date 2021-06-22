# BOJ_2960 에라토스테네스의 체

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    
    count = 0

    nums = [True] * (n+1)

    for i in range(2, len(nums) + 1):
        for j in range(i, n+1, i):
            if nums[j]:
                nums[j] = False
                count += 1
                if count == m:
                    print(j)
                    break
solution()