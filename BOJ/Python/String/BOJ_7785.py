# BOJ_7785 회사에 있는 사람

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())    
    persons = {}
    answer = []

    for _ in range(n):
        name, log  = map(str, input().rstrip().split())
        persons[name] = log

    for key, value in persons.items():
        if value == 'enter':
            answer.append(key)

    answer.sort(reverse=True)
    
    for a in answer:
        print(a)

solution()