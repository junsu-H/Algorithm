import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array1 = list(map(int, sys.stdin.readline().rstrip().split()))
    array2 = list(map(int, sys.stdin.readline().rstrip().split()))
    
    array1.sort()
    array2.sort(reverse=True)
    
    answer = 0

    for i in range(n):
        answer += array1[i] * array2[i]

    print(answer)

solution()
