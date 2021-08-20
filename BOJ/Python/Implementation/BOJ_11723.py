# BOJ_11723 집합

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    s = set()

    for _ in range(n):
        x = list(input().rstrip().split())

        if len(x) == 1:
            if x[0] == "all":
                s = set([i for i in range(1,21)])
            elif x[0] == "empty":
                s = set()
        else:
            operation, num = x[0], x[1]
            num = int(num)

            if operation == "add":
                s.add(num)
            elif operation == "remove":
                s.discard(num)
            elif operation == "check":
                if num in s:
                    print(1)
                else:
                    print(0)
            elif operation == "toggle":
                if num in s:
                    s.discard(num)
                else:
                    s.add(num)

solution()