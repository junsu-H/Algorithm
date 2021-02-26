# 선택 정렬
# 순방향

def selection_sort(array):
    
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j        
        array[i], array[min_index] = array[min_index], array[i] 
    
    return array

numbers = [6, 10, 2, 1, 4, 7, 3, 9]

print(selection_sort(numbers))