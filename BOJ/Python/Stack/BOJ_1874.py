# BOJ_1874 스택 수열

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())

    stack, answer = [], []
    count = 1

    for _ in range(1, n+1):
        data = int(input().rstrip())

        while count <= data:
            stack.append(count)
            answer.append("+")
            count += 1
        
        if stack[-1] == data:
            stack.pop()
            answer.append("-")
        else:
            print("NO")
            exit()

    print("\n".join(answer))

solution()