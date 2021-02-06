import sys

def solution():
    try:
        while True:
            a, b, c= map(int, sys.stdin.readline().rstrip().split())
            print(max(b-a, c-b)-1)
    except Exception:
        exit()

solution()