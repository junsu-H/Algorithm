import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    for _ in range(n):
        [name, kor, eng, math] = map(str, sys.stdin.readline().rstrip().split())
        array.append([name, int(kor), int(eng), int(math)])

    array.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
    
    for answer in array:
        print(answer[0])

solution()