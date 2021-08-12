# BOJ_2470 두 용액

from sys import maxsize, stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    sol = sorted(list(map(int, input().rstrip().split())))
    start, end = 0, n - 1
    max_num = maxsize
    answer = [0, 0]

    while start < end:
        total = sol[start] + sol[end]
        if abs(total) < max_num:
            max_num = abs(total)
            answer[0], answer[1] = sol[start], sol[end]

        if total < 0:
            start += 1
        else:
            end -= 1
    
    print(*answer)
    
solution()