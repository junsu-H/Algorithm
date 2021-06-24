# BOJ_1977 완전제곱수

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    m = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    answer = []
    i = 1
    
    while True:
        if i ** 2 > n:
            break

        if m <= i ** 2 and i ** 2 <= n:
            answer.append(i ** 2)
        i += 1
    if len(answer) == 0:
        print(-1)
    else:
        print(sum(answer))
        print(answer[0])

solution()