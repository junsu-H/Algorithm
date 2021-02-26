# 두 배열의 원소 교체

def solution():
    n, m = input().split()

    first_array = list(map(int, input().split()))
    second_array = list(map(int, input().split()))
    
    first_array.sort()
    second_array.sort(reverse=True)

    for i in range(int(m)):
        if first_array[i] < second_array[i]:
            first_array[i], second_array[i] = second_array[i], first_array[i]
        else:
            break
        
    print(sum(first_array))
   
solution()
