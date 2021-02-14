import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    try:
        for i in range(n):
            m = int(sys.stdin.readline().rstrip())
            if m != 0:
                array.append(m)
            else:
                array.pop()  
    except:
        print(0)

    print(sum(array))

solution()
