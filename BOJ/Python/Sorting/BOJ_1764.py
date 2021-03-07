import sys
from collections import Counter

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    first_array = [sys.stdin.readline().rstrip() for _ in range(n)]
    seconde_array = [sys.stdin.readline().rstrip() for _ in range(m)]
    
    first_array.extend(seconde_array)
    first_array.sort()
    
    count = 0
    answer = ''

    for key, value in Counter(first_array).items():
        if value >= 2:
            count += 1
            answer += key + '\n'
    
    print(count)
    print(answer.rstrip('\n'))

solution()