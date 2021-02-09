import sys

def solution():
    case_num = 1
    
    
    while True:
        l, p, v = map(int, sys.stdin.readline().rstrip().split())
        
        if l+p+v == 0:
            break
        
        answer = (v//p) * l
        answer += min((v%p), l)
        
        print("Case {0}: {1}".format(case_num, answer))
        case_num += 1
    
solution()