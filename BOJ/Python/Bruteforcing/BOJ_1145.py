# BOJ_1145 적어도 대부분의 배수

from sys import stdin

input = stdin.readline

def solution():
    number = list(map(int, input().rstrip().split()))
    count = 0
    i = 1

    while count < 3:
        count = 0
        
        for n in number:
            if i % n == 0:
                count += 1
            
            if count == 3:
                break

        i += 1

    print(i-1)

solution()