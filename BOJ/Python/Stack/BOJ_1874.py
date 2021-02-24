import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    count = 1
    result = []
    stack = []

    for i in range(1, n+1):
        data = int(sys.stdin.readline().rstrip())

        while count <= data:
            stack.append(count)
            count += 1
            result.append("+")
        
        if stack[-1] == data:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            exit()

    print("\n".join(result))

solution()