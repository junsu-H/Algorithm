import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    count = 0
    start = 0
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))

    array = sorted(array, key = lambda x: [x[1], x[0]])

    for i in array:
        if i[0] >= start:
            start = i[1]
            count += 1
    
    print(count)
    
solution()