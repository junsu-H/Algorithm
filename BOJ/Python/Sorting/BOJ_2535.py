import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []

    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    array.sort(reverse=True, key = lambda x: x[2])

    print(array[0][0], array[0][1])
    print(array[1][0], array[1][1])

    if array[0][0] == array[1][0]: 
        print(array[3][0], array[3][1])

    else: 
        print(array[2][0], array[2][1])
    
solution()
