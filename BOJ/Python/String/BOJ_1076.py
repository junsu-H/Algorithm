# BOJ_1076 저항

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    # multifly = {
    #         "black": 1,
    #         "brown": 10,
    #         "red": 100,
    #         "orange": 1000,
    #         "yellow": 10000,
    #         "green": 100000,
    #         "blue": 1000000,
    #         "violet": 10000000,
    #         "grey": 100000000,
    #         "white": 1000000000
    # }
    values =  {
            "black": 0,
            "brown": 1,
            "red": 2,
            "orange": 3,
            "yellow": 4,
            "green": 5,
            "blue": 6,
            "violet": 7,
            "grey": 8,
            "white": 9
    }

    color = [sys.stdin.readline().rstrip() for _ in range(3)]

    print(int(str(values[color[0]]) + str(values[color[1]])) * 10**values[color[2]])

solution()