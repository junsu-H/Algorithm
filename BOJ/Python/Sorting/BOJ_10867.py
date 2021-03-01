import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    array = list(set(array))    
    array.sort()
    
    for _ in array:
        print(_, end=' ')

solution()