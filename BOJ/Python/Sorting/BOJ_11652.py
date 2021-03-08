import sys
from collections import Counter

def solution():
    n = int(sys.stdin.readline().rstrip())

    card_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    answer = Counter(sorted(card_list)).most_common(1)[0][0]

    print(answer)

solution()