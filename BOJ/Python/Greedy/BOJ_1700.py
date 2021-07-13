# BOJ_1700 멀티탭 스케줄링

from sys import stdin

input = stdin.readline

def solution():
    n, k = map(int, input().rstrip().split())
    multitab = list(map(int, input().rstrip().split()))
    plugs = []
    answer = 0

    for i in range(k):
        if multitab[i] in plugs:
            continue
        
        if len(plugs) < n:        
            plugs.append(multitab[i])
            continue

        indexs = []

        for j in range(n):
            try:
                indexs.append(multitab[i:].index(plugs[j]))
            except:
                indexs.append(101)
        
        del plugs[indexs.index(max(indexs))]
        plugs.append(multitab[i])
        answer += 1

    print(answer)

solution()