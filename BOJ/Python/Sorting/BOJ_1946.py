import sys

def solution():
    for _ in range(int(sys.stdin.readline().rstrip())):
        n = int(sys.stdin.readline().rstrip())
        array = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
        array.sort(key = lambda x: x[0])

        answer = 1
        ranking = array[0][1]

        for i in range(1, n):
            ranking = min(ranking, array[i][1])
            if ranking == array[i][1]:
                answer += 1
        
        print(answer)

solution()