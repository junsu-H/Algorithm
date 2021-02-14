import sys
import collections

def solution():
    n = int(sys.stdin.readline().rstrip())

    result = []

    for _ in range(n):
        result.append(sys.stdin.readline().rstrip())

    result.sort()
    count = collections.Counter(result)

    print(count.most_common(n=1)[0][0])

solution()