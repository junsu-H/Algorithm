import sys
import re

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    
    for _ in range(n):
        temp = [] 
        name = sys.stdin.readline().rstrip()
        length = len(name)
        plus = re.sub('[^0-9]', '0', name)
        if len(plus) > 0:
            plus = sum(map(int, plus))
        temp.append(name)
        temp.append(length)
        temp.append(plus)
        array.append(temp)
    
    array.sort(key=lambda x: (x[1], x[2], x[0]))
    
    for _ in array:
        print(_[0])

solution()