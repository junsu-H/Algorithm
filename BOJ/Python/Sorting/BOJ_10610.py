import sys

def solution():
    n = sys.stdin.readline().rstrip()

    temp_sum = 0

    if '0' not in n:
        print(-1)
    else:
        for i in n:
            temp_sum += int(i)
        
        if temp_sum%3 != 0:
            print(-1)
        else:
            print(''.join(sorted(n, reverse=True)))

solution()
