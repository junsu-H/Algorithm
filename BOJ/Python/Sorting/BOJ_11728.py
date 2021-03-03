import sys

def solution():
    n, m= map(int, sys.stdin.readline().rstrip().split())
    first_array = list(map(int, sys.stdin.readline().rstrip().split()))
    second_array = list(map(int, sys.stdin.readline().rstrip().split()))

    answer = first_array + second_array
    answer.sort()

    for num in answer:
        print(num, end=' ')

solution()