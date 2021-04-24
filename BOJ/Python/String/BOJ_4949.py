# BOJ_4949 균형잡힌 세상0

import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    while True:
        string = sys.stdin.readline().rstrip()
        
        if string == '.':
            break

        answer = True
        answer_stack = []

        for check in string:
            if check == '(' or check == '[':
                answer_stack.append(check)
            
            elif check == ')':
                if len(answer_stack) == 0:
                    answer = False
                    break
                if answer_stack[-1] == '(':
                    answer_stack.pop()
                    answer = True
                else:
                    answer = False
                    break
            
            elif check == ']':
                if len(answer_stack) == 0:
                    answer = False
                    break
                if answer_stack[-1] == '[':
                    answer_stack.pop()
                    answer = True
                else:
                    answer = False
                    break

        if answer and len(answer_stack) == 0:
            print("yes")
        else:
            print("no")
        
solution()