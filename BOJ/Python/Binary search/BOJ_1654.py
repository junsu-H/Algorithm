# BOJ_1654 랜선 자르기

from sys import stdin

input = stdin.readline

def solution():
    k, n = map(int, input().rstrip().split())
    
    lans = [int(input().rstrip()) for _ in range(k)]

    start, end = 1, max(lans)

    while True:
        if start > end:
            break

        mid = (start + end) // 2
        count = 0

        for lan in lans:
            count += lan // mid
        
        if count < n:          
            end = mid - 1 

        elif count >= n:          
            start = mid + 1

    print(end)

solution()