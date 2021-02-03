import sys

def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())

    coin = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    coin.sort(reverse=True)

    num = 0
    answer = 0
    
    for i in coin: 
        if k >= i:
            num = k // i
            k -= num * i
            answer += num    
        if k == 0:
            break
    print(answer)

solution()