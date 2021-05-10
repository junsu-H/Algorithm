# BOJ_10828 스택

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    answer = []

    for i in range(len(array)):
        if array[i][0] == 'push':
            answer.append(array[i][1])
        elif array[i][0] == 'pop':
            if not answer:
                print(-1)
            else:
                print(answer.pop())
        elif array[i][0] == 'size':
            print(len(answer))
        elif array[i][0] == 'empty':
            # 비었으면
            if not answer:
                print(1)
            # 안 비었으면
            else:
                print(0)
        elif array[i][0] == 'top':
            if len(answer) == 0:
                print(-1)
            else:
                print(answer[-1])

solution()