import sys

def solution():
    x = int(sys.stdin.readline().rstrip())
    
    answer = 0
    while x != 1:
        if x % 3 == 0:
            x //= 3
            answer += 1
        elif x % 3 == 1:
            x -= 1
            answer += 1
        if x % 2 == 0:
            x = x//2
            answer += 1

        # else:
        #     x -= 1
        #     answer += 1

    print(answer)
        
solution()