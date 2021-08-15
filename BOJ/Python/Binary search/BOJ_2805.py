# BOJ_2805 나무 자르기

from sys import stdin

input = stdin.readline

def solution():
    n, m = map(int, input().rstrip().split())
    trees = list(map(int, input().rstrip().split()))

    start, end = 1, max(trees)

    while True:
        if start > end:
            break
        
        tree_sum = 0
        mid = (start + end) // 2
        
        for tree in trees:
            if tree >= mid:
                tree_sum += tree - mid
            
        if tree_sum >= m:
            start = mid + 1
        else:
            end = mid- 1
    
    print(end)
        
solution()