import sys

def solution():
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    array.sort()
    
    for i in array:
        print(i, end=' ')

solution()