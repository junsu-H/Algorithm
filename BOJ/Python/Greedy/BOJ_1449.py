import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, l = map(int, sys.stdin.readline().rstrip().split())

    array = list(map(int, sys.stdin.readline().rstrip().split()))
    array.sort()
    
    start = 0
    count = 0

    for location in array:
        if start < location:
            start = location + l - 1
            count += 1

    print(count)

solution()