import sys

def solution():

    n, k = map(int, sys.stdin.readline().rstrip().split())
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    array.sort()

    print(array[k-1])

solution()
