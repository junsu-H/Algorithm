import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    
    array.sort()

    for num in array:
        print(num, end=' ')

solution()