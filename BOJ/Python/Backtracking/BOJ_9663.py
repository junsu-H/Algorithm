import sys

def is_promising(x, y, n, current):
    for i in range(x):
        if y == current[i] or abs(y - current[i]) == x-i:
            return False
    return True

def queen(x, queen_n, current):
    if x == queen_n:
        return 1

    count = 0

    for y in range(queen_n):
        if is_promising(x, y, n, current):
            current[x] = y
            count += queen(x=1, queen_n, current)
    
    return count


def solution(n):
    sys.setrecursionlimit(10000)
    
    array = [0] * n

    answer = queen(0, n, array)

solution(int(sys.stdin.readline().rstrip()))