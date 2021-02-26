# 위에서 아래로

def solution():
    n = int(input())
    array = []
    for i in range(n):
        m = int(input())
        array.append(m)

    array.sort(reverse=True)
    for i in array:
        print(i, end=' ')
    

solution()
