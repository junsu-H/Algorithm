import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    t = int(sys.stdin.readline().rstrip())
    array = []
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        for j in range(n):
            array.append(list(sys.stdin.readline().rstrip().split()))
            array.sort(key = lambda x: int(x[1]), reverse=True)
        print(array[0][0])

solution()