import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    n_set = set(map(int, sys.stdin.readline().rstrip().split()))
   
    m = int(sys.stdin.readline().rstrip())
    m_list = list(map(int, sys.stdin.readline().rstrip().split()))
    
    for i in range(m):
        if m_list[i] in n_set:
            print(1, end=' ')
        else:
            print(0, end=' ')

solution()
