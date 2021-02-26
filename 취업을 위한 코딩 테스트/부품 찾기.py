def binary_search(array, target, start, end):
    # while start <= end:
    if start > end:
        return None
    
    mid = (start+end)//2
    if target == array[mid]:
        return array[mid]
        
    elif array[mid]<target:
        # start = mid + 1
        return binary_search(array, target, mid + 1, end)
    elif array[mid]>target:
        # end = mid -1
        return binary_search(array, target, start, mid-1)
    else:
        return None

def solution():
    n = int(input())
    
    lst = list(map(int, input().split()))

    lst.sort()

    m = int(input())

    check = list(map(int, input().split()))

    for i in check:
        result = binary_search(lst, i, 0, n-1)
        if result != None:
            print("yes", end=' ')
        else:
            print("no", end=' ')

solution()
