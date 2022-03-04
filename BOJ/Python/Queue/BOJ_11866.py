# BOJ_11866 요세푸스 문제 0

from sys import stdin

input = stdin.readline

def solution():
    n, k = map(int, input().rstrip().split())
    people = list(range(1, n+1))
    answer, index = [], 0

    while people:
        index = (index + (k-1)) % len(people)
        answer.append(str(people.pop(index)))
    
    print("<{0}>".format(', '.join(answer)))   

solution()