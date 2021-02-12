import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    array = []
    answer = []

    for i in range(n):
        array.append((int(sys.stdin.readline().rstrip()), i))

    sort_array = sorted(array)

    for i in range(n):
        answer.append(sort_array[i][1] - array[i][1])

    print(max(answer) + 1)

solution()
