# 개미 전사

def solution():
    n = int(input())
    array = list(map(int, input().split()))

    odd = 0
    even = 0
    for i in range(len(array)):
        if i%2 != 0:
            odd += array[i]
        elif i%2 == 0:
            even += array[i]
    print(max(odd, even))

solution()


# def solution():
#     n = int(input())
#     array = list(map(int, input().split()))

#     d = [0] * 100

#     d[0] = array[0]
#     d[1] = max(array[0], array[1])
    
#     for i in range(2, n):
#         d[i] = max(d[i-1], d[i-2] + array[i])
    
#     print(d[n-1])

# solution()