import sys

def solution():
    t = int(sys.stdin.readline().rstrip())

    fibo = [0, 1]
    
    for i in range(2, 46):
        fibo.append(fibo[i-2] + fibo[i-1])

    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        answer = []
    
        while n:
            for j in range(46):
                if fibo[j] <= n:
                    temp = fibo[j]

            n -= temp
            answer.append(temp)            
    
    for _ in range(len(answer)-1, -1, -1):
        print(answer[_], end=' ')

solution()