import sys

def solution():
    array = sys.stdin.readline().rstrip().split('-')
    
    answer = 0
    
    for i in array[0].split('+'):
        answer += int(i)
    
    for i in array[1:]:
        for j in i.split('+'):
            answer -= int(j)
            
    print(answer)

solution()
