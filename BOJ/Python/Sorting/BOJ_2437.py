import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    
    array.sort()

    target = 1

    for i in array:
        if target < i:
            break
        target += i

    print(target)

solution()