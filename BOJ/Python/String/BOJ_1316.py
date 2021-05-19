# BOJ_1316 그룹 단어 체커

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())

    answer = 0

    for _ in range(n):
        check = True
        word = sys.stdin.readline().rstrip()
        for i in range(1, len(word)):
            if word[i-1] != word[i]:
                if word[i-1] in word[i:]:
                    check = False
                    break
        
        if check:
            answer += 1

    print(answer)

solution()