# BOJ_2628 종이자르기

from sys import stdin

input = stdin.readline

def solution():
    x, y = map(int, input().rstrip().split())
    t = int(input().rstrip())
    x_list, y_list = [0, x], [0, y]
    max_x, max_y = 0, 0

    for _ in range(t):
        xy_num, cut_num = map(int, input().rstrip().split())
        
        if xy_num == 1:
            x_list.append(cut_num)
        else:
            y_list.append(cut_num)

    x_list.sort()
    y_list.sort()


    for i in range(len(x_list)-1):
        max_x = max(max_x, x_list[i+1] - x_list[i])
    
    for i in range(len(y_list)-1):
        max_y = max(max_y, y_list[i+1] - y_list[i])

    print(max_x * max_y)

solution()