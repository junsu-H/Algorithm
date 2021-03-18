import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        note1 = set(map(int, sys.stdin.readline().rstrip().split()))
        m = int(sys.stdin.readline().rstrip())
        note2 = list(map(int, sys.stdin.readline().rstrip().split()))
        for number in note2:
            if number in note1:
                print(1)
            else:
                print(0)

solution()