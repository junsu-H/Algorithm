# BOJ_2309 일곱 난쟁이

from sys import stdin

input = stdin.readline

def solution():
    dwarf = [int(input().rstrip()) for _ in range(9)]
    dwarf.sort()
    answer = sum(dwarf)

    for i in range(9):
        for j in range(i+1, 9):
            if answer - dwarf[i] - dwarf[j] == 100:
                for k in range(9):
                    if k == i or k == j:
                        continue
                    else:
                        print(dwarf[k])
                exit()

solution()