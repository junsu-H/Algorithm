import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    answer = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    answer.sort(key = lambda x: (int(x[3]), int(x[2]), int(x[1])))

    print(answer[-1][0])
    print(answer[0][0])

solution()
