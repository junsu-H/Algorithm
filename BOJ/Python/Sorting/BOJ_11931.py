import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    array.sort(reverse=True)

    for i in array:
        print(i)

solution()