import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    coin = [500, 100, 50, 10, 5, 1]

    remain = 1000-n

    temp = 0
    count = 0
    
    for i in coin:
        if remain >= i:
            temp = remain // i
            remain -= (temp * i)
            count += temp

    print(count)
    
solution()