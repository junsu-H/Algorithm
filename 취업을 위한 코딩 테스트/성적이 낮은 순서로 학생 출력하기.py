# 성적이 낮은 순서로 학생 출력하기

def solution():
    n = int(input())
    array = []

    for i in range(n):
        input_data = input().split()
        array.append((input_data[0], input_data[1]))

    array.sort(key=lambda x : input_data[1])
    for i in array:
        print(i[0], end=' ')
    

solution()
