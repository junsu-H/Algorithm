import sys

def solution():
    n = sys.stdin.readline().rstrip()

    answer = 1

    for i in range(len(n)-1):
        if n[i] != n[i+1]:
            answer += 1

    print(answer//2)

solution()
