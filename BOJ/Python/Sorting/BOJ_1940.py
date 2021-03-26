import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    left, right = 0, n-1
    count = 0

    array = list(map(int, sys.stdin.readline().rstrip().split()))
    array.sort()
    
    while left < right:
        if array[left] + array[right] == m:
            count += 1
            left += 1
            right -= 1
        elif array[left] + array[right] < m:
            left += 1
        else:
            right -= 1
    
    print(count)

solution()