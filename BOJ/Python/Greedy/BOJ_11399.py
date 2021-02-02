import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    array = list(map(int, sys.stdin.readline().rstrip().split()))

    array.sort()
    answer = 0
    
    for i in range(n):
        answer += array[i] * (n-i)

    print(answer)

solution()