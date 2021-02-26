import sys
from collections import Counter

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    
    for _ in range(n):
        array.append(int(sys.stdin.readline().rstrip()))
    
    array.sort()

    mean = round(sum(array) / n)
    median = array[n//2]
    mode = Counter(array)
    scope = max(array)-min(array)

    print(mean)
    print(median)
    if n > 1 and mode.most_common()[0][1]==mode.most_common()[1][1]:
        print(mode.most_common(2)[1][0])
    else:
        print(mode.most_common(1)[0][0])
    print(scope)

solution()