# BOJ_16968 차량 번호판 1

from sys import stdin

input = stdin.readline

def solution():
    string = input().rstrip()
    answer = 26 if string[0] == "c" else 10
    for i in range(1, len(string)):
        if string[i-1] == string[i] and string[i] == "c":
            answer *= 25
        elif string[i-1] == string[i] and string[i] == "d":
            answer *= 9
        elif string[i-1] != string[i] and string[i] == "c":
            answer *= 26
        elif string[i-1] != string[i] and string[i] == "d":
            answer *= 10

    print(answer)

solution()