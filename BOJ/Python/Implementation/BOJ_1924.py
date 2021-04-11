# BOJ_1924 2007년

import sys
sys.setrecursionlimit(10 ** 9)
import calendar

def solution():
    m, d = map(int, sys.stdin.readline().rstrip().split())
    
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    k = calendar.weekday(2007, m, d)
    
    print(day[k])

solution()