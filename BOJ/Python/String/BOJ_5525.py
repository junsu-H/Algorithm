# BOJ_5525 IOIOI

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    m = int(input().rstrip())
    string = input().rstrip()
    
    i = 1
    pattern = 0
    answer = 0

    while True:
        if i >= m -1:
            break

        if string[i-1] == "I" and string[i] == "O" and string[i+1] == "I":
            pattern += 1
            if pattern == n:
                pattern -= 1
                answer += 1
            i += 1
        else:
            pattern = 0
        i += 1

    print(answer)

solution()