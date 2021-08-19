# BOJ_19941 햄버거 분배

from sys import stdin

input = stdin.readline

def solution():
    n, k = map(int, input().rstrip().split())
    bench = list(map(str, input().rstrip()))
    answer = 0
    
    for i in range(n):
        if bench[i] == "P":
            for j in range(i-k, i+k+1):
                if 0 <= j and j < n and bench[j] == "H":
                    answer += 1
                    bench[j] = "0"
                    break
    print(answer)

solution()