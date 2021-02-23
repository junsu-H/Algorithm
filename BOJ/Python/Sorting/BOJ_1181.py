import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    sort_array = []

    for _ in range(n):
        array.append(sys.stdin.readline().rstrip())
    
    array = list(set(array))

    for i in array:
        sort_array.append((len(i), i))
    
    sort_array.sort()
    
    for i in range(len(sort_array)):
        print(sort_array[i][1])

solution()