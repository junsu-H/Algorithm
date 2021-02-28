import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def solution():
    n = int(sys.stdin.readline().rstrip())
    print(factorial(n))

solution()