# BOJ_4999 아!

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    hwan = sys.stdin.readline().rstrip()
    doctor = sys.stdin.readline().rstrip()

    if len(hwan) >= len(doctor) and doctor in hwan:
        print("go")
    else:
        print("no")

solution()
