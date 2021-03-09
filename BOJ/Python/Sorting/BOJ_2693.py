import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        a_list = list(map(int, sys.stdin.readline().rstrip().split()))
        a_list.sort(reverse=True)
        print(a_list[2])
    
solution()