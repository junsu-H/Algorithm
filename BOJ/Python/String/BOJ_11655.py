# BOJ_11655 ROT13 

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    string = sys.stdin.readline().rstrip()
    answer = ''
    for s in string:
        if s.isupper():
            if ord(s)+ 13 <= 90:
                answer += chr(ord(s)+13)
            else:
                answer += chr(ord(s)-13)
    
        elif s.islower():
            if ord(s)+ 13 <= 122:
                answer += chr(ord(s)+13)
            else:
                answer += chr(ord(s)-13)
        else:
            answer += s

    print(answer)
    
solution()