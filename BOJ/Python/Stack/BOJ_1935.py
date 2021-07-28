# BOJ_1935 후위 표기식2

from sys import stdin

input = stdin.readline

def solution():
    n = int(input().rstrip())
    postfix = input().rstrip()
    stack = []
    alpha = {}

    for i in range(n):
        alpha[chr(65+i)] = input().rstrip()
    
    for p in postfix:
        if p.isalpha():
            stack.append(alpha[p])
        else:
            second_num = float(stack.pop())
            first_num = float(stack.pop())

            if p == "+":
                stack.append(first_num + second_num)
            elif p == "-":
                stack.append(first_num - second_num)
            elif p == "*":
                stack.append(first_num * second_num)
            elif p == "/":
                stack.append(first_num / second_num)

    print("{:0.2f}".format(stack[0]))
    
solution()