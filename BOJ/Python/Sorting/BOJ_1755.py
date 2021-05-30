# BOJ_1755 숫자놀이

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    m, n = map(int, sys.stdin.readline().rstrip().split())

    number_dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", 
                    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

    answer = []
    for i in range(m, n+1):
        alpha = ''.join([number_dict[key] for key in str(i)])
        answer.append([i, alpha])

    answer.sort(key=lambda x:x[1])

    for i in range(len(answer)):
        if i > 0 and i % 10 == 0:
            print()
        print(answer[i][0], end=' ')
        
solution()