import sys
sys.setrecursionlimit(10 ** 9)

count = 0

def merge_split(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_split(array[:mid])
    right = merge_split(array[mid:])

    return merge(left, right)

def merge(left, right):
    global count

    merged = []
    left_point, right_point = 0, 0

    # case1: left/right 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
            count += len(left) - left_point
        else:
            merged.append(left[left_point])
            left_point += 1
    
    # case2: left만 남아있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3: right만 남아있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    merge_split(array)
    print(count)

solution()