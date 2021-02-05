import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    
    array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    array.sort(reverse=True)
    
    answer = [array[i]*(i+1) for i in range(len(array))]
    
    print(max(answer))

solution()
