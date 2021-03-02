import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []

    for _ in range(n):
        [x_pos, y_pos] = map(int, sys.stdin.readline().rstrip().split())
        array.append([x_pos, y_pos])

    array.sort(key = lambda x: (x[1], x[0]))
    
    for answer in array:
        print(answer[0], answer[1])

solution()