# 삽입 정렬
# 역방향

def insert_sort(array):
    
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j] 
    
    return array

numbers = [6, 10, 2, 1, 4, 7, 3, 9]

print(insert_sort(numbers))