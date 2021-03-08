import sys

def solution():
    w_list = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
    k_list = [int(sys.stdin.readline().rstrip()) for _ in range(10)]

    w_list.sort(reverse=True)
    k_list.sort(reverse=True)

    print(sum(w_list[:3]), sum(k_list[:3]))
    
solution()