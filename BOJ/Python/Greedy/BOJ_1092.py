# BOJ_1092 배

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    cranes = sorted(list(map(int, input().rstrip().split())), reverse = True)
    m = int(input().rstrip())
    boxes = sorted(list(map(int, input().rstrip().split())), reverse = True)

    answer = 0

    if cranes[0] < boxes[0]:
        print(-1)
    else:
        while True:
            if not boxes:
                break
            answer += 1

            for crane in cranes:
                for j in range(len(boxes)):
                    if boxes[j] <= crane:
                        boxes.pop(j)
                        break
    print(answer)

solution()