# BOJ_2729 이진수 덧셈

T = int(input())

for _ in range(T):
    first, second = input().split()
    first = int(first, 2)
    second = int(second, 2)
    print(bin(first+second)[2:])