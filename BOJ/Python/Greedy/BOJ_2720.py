import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        quarter = 0
        dime = 0
        nickel = 0
        penny = 0

        n = int(sys.stdin.readline().rstrip())
        while True:
            if n >= 25:
                quarter = n // 25
                n %= 25
            elif n >= 10:
                dime = n // 10
                n %= 10
            elif n >= 5:
                nickel =  n // 5
                n %= 5
            else:
                penny = n // 1
                n %= 1
            
            if n == 0:
                break

        print(quarter, dime, nickel, penny)

solution()