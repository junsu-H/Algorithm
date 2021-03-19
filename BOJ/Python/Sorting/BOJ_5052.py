import sys
sys.setrecursionlimit(10 ** 9)

def check(data):
    data.sort()
    for p1, p2, in zip(data, data[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution():
    t = int(sys.stdin.readline().rstrip())

    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        num_list = [sys.stdin.readline().rstrip() for _ in range(n)]

        if check(num_list):
            print("YES")
        else:
            print("NO")

solution()