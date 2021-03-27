import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    array = list(map(int, sys.stdin.readline().rstrip().split()))
    start, end = 0, 0
    count = 0 

    while start <= end and end <= n :

        if sum(array[start:end]) == m:
            end += 1
            count += 1
        elif sum(array[start:end]) > m:
            start += 1
        elif sum(array[start:end]) < m:
            end += 1
    
    print(count)

solution()