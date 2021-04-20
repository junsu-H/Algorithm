# BOJ_10816 숫자 카드 2

import sys
sys.setrecursionlimit(10 ** 9)
from collections import Counter

def solution():
    n = int(sys.stdin.readline().rstrip())
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))

    m = int(sys.stdin.readline().rstrip())
    m_list = list(map(int, sys.stdin.readline().rstrip().split()))

    temp = Counter(n_list)
    answer = ''

    for number in m_list:
        if number in temp:
            answer += str(temp[number]) + ' '
        else: 
            answer += '0 '
    
    print(answer.rstrip())

solution()