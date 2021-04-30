# BOJ_2212 센서

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    
    array.sort()
    
    start, end = 0, 1
    answer = []

    if(n <= k):
        print(0)
    else:
        while True:
            if start == len(array)-1 and end == len(array):
                break

            answer.append(array[end] - array[start])

            start += 1
            end += 1
        answer.sort(reverse=True)

        for i in range(k-1):
            answer.pop(0)

        print(sum(answer))

solution()