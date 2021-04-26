# BOJ_14659 한조서열정리하고옴ㅋㅋ 

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    persons = list(map(int, sys.stdin.readline().rstrip().split()))

    max_person = persons[0]
    answer = 0
    count = 0

    for i in range(1, n):
        if persons[i] > max_person:
            max_person = persons[i]
            count = 0
        else:
            count += 1

        answer = max(answer, count)

    print(answer)

solution()