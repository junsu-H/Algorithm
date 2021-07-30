# BOJ_7568 덩치

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())

    people = [list(map(int, input().rstrip().split())) for i in range(n)]

    for i in range(len(people)):
        rank = 1

        for j in range(len(people)):
            
            if not (people[i][0] == people[j][0] or people[i][1] == people[j][1]):
                if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                    rank += 1
        print(rank)

solution()