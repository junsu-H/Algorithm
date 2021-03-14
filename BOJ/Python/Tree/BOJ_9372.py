import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())

        for _ in range(m):
            temp_a, temp_b = map(int, sys.stdin.readline().rstrip().split())
        
        print(n-1)

solution()