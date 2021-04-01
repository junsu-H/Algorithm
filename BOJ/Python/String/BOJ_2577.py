import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    c = int(sys.stdin.readline().rstrip())
    
    total = list(map(str, str(a * b * c)))
    answer = [0] * 10

    for num in total:
        answer[int(num)] += 1

    print('\n'.join(map(str, answer)))

solution()
