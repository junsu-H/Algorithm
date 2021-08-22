# BOJ_1193 분수찾기

from sys import stdin

input = stdin.readline

def solution():
    number = int(input().rstrip())
    line = 1

    while True:
        if number <= line:
            break
        number -= line
        line += 1

    if line % 2 == 0:
        molecule = number
        denominator = line - number + 1
    else:
        molecule = line - number + 1
        denominator = number
    
    print(str(molecule) + "/" + str(denominator))

solution()