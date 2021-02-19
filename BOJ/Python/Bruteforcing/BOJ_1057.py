import sys

def solution():
    n, kim, lim = map(int, sys.stdin.readline().rstrip().split())
    count = 0
    
    while (kim != lim):
        kim -= kim//2
        lim -= lim//2
        count += 1
    
    print(count)

solution()
