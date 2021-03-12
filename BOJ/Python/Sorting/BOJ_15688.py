import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    
    for _ in range(n):
        array.append(int(sys.stdin.readline().rstrip()))
    
    array.sort()
    print('\n'.join(map(str, array)))

solution()