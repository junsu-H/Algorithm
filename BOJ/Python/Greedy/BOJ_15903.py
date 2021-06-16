# BOJ_15903 카드 합체 놀이

import sys

sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cards = list(map(int, sys.stdin.readline().rstrip().split()))

    for _ in range(m):
        cards.sort()
        cards[0] = cards[1] = cards[0] + cards[1]

    print(sum(cards))

solution()